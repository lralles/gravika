# Copyright (C) 2026 Leonardo Rezende Alles
# SPDX-License-Identifier: AGPL-3.0-or-later
import argparse
import sys
import os
from pathlib import Path
import pandas as pd

from src.models.graph_loader import GraphLoader
from src.models.centrality_service import CentralityAnalysisService, centrality_functions


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Calculate centrality diff scores for graph node removal analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --file-type tsv --file-location data.tsv --nodes A,B,C --centralities degree,betweenness
  %(prog)s --file-type gexf --file-location graph.gexf --nodes 1,2,3 --centralities degree,closeness,eigenvector
  %(prog)s --file-type cys --file-location network.cys --nodes node1 --centralities katz --output results.csv

Available centralities: degree, unnormalized_degree, betweenness, closeness, eigenvector, katz
        """
    )
    
    parser.add_argument(
        '--file-type',
        type=str,
        required=True,
        choices=['tsv', 'gexf', 'cys'],
        help='Type of the graph file (tsv, gexf, or cys)'
    )
    
    parser.add_argument(
        '--file-location',
        type=str,
        required=True,
        help='Path to the graph file'
    )
    
    parser.add_argument(
        '--nodes',
        type=str,
        default='',
        help='Comma-separated list of nodes to remove (e.g., A,B,C or 1,2,3). Leave empty to calculate centrality without removal.'
    )
    
    parser.add_argument(
        '--centralities',
        type=str,
        required=True,
        help=f'Comma-separated list of centralities to calculate. Available: {", ".join(centrality_functions.keys())}'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='centrality_results.csv',
        help='Output CSV file path (default: centrality_results.csv)'
    )
    
    parser.add_argument(
        '--edge1',
        type=str,
        default='source',
        help='Column name for source node (TSV only, default: source)'
    )
    
    parser.add_argument(
        '--edge2',
        type=str,
        default='target',
        help='Column name for target node (TSV only, default: target)'
    )
    
    parser.add_argument(
        '--weight',
        type=str,
        default='weight',
        help='Column name for edge weight (TSV only, default: weight)'
    )
    
    parser.add_argument(
        '--network-name',
        type=str,
        default=None,
        help='Network name to load from CYS file (CYS only, defaults to first network)'
    )
    
    parser.add_argument(
        '--directed',
        action='store_true',
        help='Create a directed graph (default: undirected)'
    )
    
    parser.add_argument(
        '--remove-self-edges',
        action='store_true',
        default=True,
        help='Remove self-edges from the graph (default: True)'
    )
    
    parser.add_argument(
        '--remove-zero-degree',
        action='store_true',
        help='Remove nodes with degree 0'
    )
    
    parser.add_argument(
        '--largest-component',
        action='store_true',
        help='Use only the largest connected component'
    )
    
    return parser.parse_args()


def validate_inputs(args):
    if not os.path.exists(args.file_location):
        print(f"Error: File not found: {args.file_location}", file=sys.stderr)
        sys.exit(1)
    
    requested_centralities = [c.strip() for c in args.centralities.split(',')]
    invalid_centralities = [c for c in requested_centralities if c not in centrality_functions]
    
    if invalid_centralities:
        print(f"Error: Invalid centralities: {', '.join(invalid_centralities)}", file=sys.stderr)
        print(f"Available centralities: {', '.join(centrality_functions.keys())}", file=sys.stderr)
        sys.exit(1)
    
    return requested_centralities


def parse_nodes(nodes_str):
    if not nodes_str or nodes_str.strip() == '':
        return []
    
    nodes = [n.strip() for n in nodes_str.split(',')]
    
    parsed_nodes = []
    for node in nodes:
        try:
            parsed_nodes.append(int(node))
        except ValueError:
            try:
                parsed_nodes.append(float(node))
            except ValueError:
                parsed_nodes.append(node)
    
    return parsed_nodes


def main():
    args = parse_arguments()
    
    requested_centralities = validate_inputs(args)
    
    print(f"Loading graph from {args.file_location}...")
    
    loader = GraphLoader()
    
    try:
        graph = loader.load(
            edge1=args.edge1,
            edge2=args.edge2,
            weight=args.weight,
            path=args.file_location,
            remove_self_edges=args.remove_self_edges,
            network_name=args.network_name,
            directed=args.directed
        )
        
        print(f"Graph loaded: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")
        
        graph = loader.process_graph(
            graph,
            remove_zero_degree=args.remove_zero_degree,
            use_largest_component=args.largest_component
        )
        
        if args.remove_zero_degree or args.largest_component:
            print(f"Graph processed: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")
        
    except Exception as e:
        print(f"Error loading graph: {e}", file=sys.stderr)
        sys.exit(1)
    
    nodes_to_remove = parse_nodes(args.nodes)
    
    if nodes_to_remove:
        print(f"Removing nodes: {nodes_to_remove}")
        
        missing_nodes = [n for n in nodes_to_remove if n not in graph.nodes()]
        if missing_nodes:
            print(f"Warning: The following nodes are not in the graph: {missing_nodes}", file=sys.stderr)
            nodes_to_remove = [n for n in nodes_to_remove if n in graph.nodes()]
            if not nodes_to_remove:
                print("Error: None of the specified nodes exist in the graph", file=sys.stderr)
                sys.exit(1)
    else:
        print("No nodes to remove - calculating centrality for all nodes")
    
    print(f"Calculating centralities: {', '.join(requested_centralities)}")
    
    analysis_service = CentralityAnalysisService()
    
    try:
        df, impact, diameter_info = analysis_service.compute(
            graph,
            nodes_to_remove,
            requested_centralities
        )
        
        print(f"\nAnalysis complete!")
        print(f"Diameter before removal: {diameter_info['before']}")
        print(f"Diameter after removal: {diameter_info['after']}")
        
        df.index.name = 'Node'
        
        output_path = Path(args.output)
        df.to_csv(output_path)
        
        print(f"\nResults saved to: {output_path.absolute()}")
        print(f"Total nodes in results: {len(df)}")
        
        if len(df) > 0:
            print("\nPreview of results (first 5 rows):")
            print(df.head().to_string())
        
    except Exception as e:
        print(f"Error during analysis: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
