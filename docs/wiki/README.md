# User Guide

Welcome to the Graph Centrality Analysis application user guide.

## Quick Start

The Graph Centrality Analysis tool helps you understand how removing nodes affects centrality measures in networks. You can analyze your own graph data or explore with built-in random graphs.

## Documentation

- [Getting Started](getting-started.md) - Installation and first steps for GUI and CLI
- [Workflow Guide](workflow.md) - Complete analysis workflow for GUI and CLI
- [File Formats](file-formats.md) - Supported input formats
- [Features](features.md) - Available analysis options for GUI and CLI

## Quick Workflow

### GUI
1. **Load Graph**: Select a file (TSV, CYS, GEXF) or use a random graph
2. **Configure**: Set column mappings for TSV files or select network from CYS
3. **Preview**: View graph structure and adjacency list
4. **Select**: Choose nodes to remove and centrality measure
5. **Analyze**: Run the analysis to see impact on remaining nodes
6. **Visualize**: Explore results in table and graph views
7. **Export**: Save results and visualizations

### CLI
1. **Load Graph**: Pass `--file-type` and `--file-location`
2. **Configure**: Optional format flags (`--edge1`, `--edge2`, `--weight`, `--network-name`) and processing flags
3. **Select**: Set `--nodes` and `--centralities`
4. **Analyze**: Run one command for full analysis
5. **Export**: Save table output with `--output` as CSV