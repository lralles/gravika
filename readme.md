# Gravika

A comprehensive tool for analyzing how node removal affects centrality measures in network graphs. Supports multiple file formats and provides interactive visualization of network structure and analysis results.

The tool has 2 versions:
- GUI for exploratory use and visualization
- CLI for bigger graphs and faster computations

## Features

- **Multiple File Formats**: TSV, CYS (Cytoscape), and GEXF support
- **Random Graph Generation (GUI only)**: Built-in generators for testing and exploration
- **Centrality Measures**: Degree (Normalized and Unnormalized), Betweenness, Closeness, Eigenvector and Katz
- **Interactive Visualization (GUI only)**: Graph plots with impact highlighting and customizable display options
- **Export Capabilities**: Save results in CSV, SVG, CYS (GUI) and CSV (CLI)

## CLI Quick Start

```bash
python3 -m src.application.cli \
  --file-type tsv \
  --file-location data.tsv \
  --nodes A,B,C \
  --centralities degree,betweenness \
  --output results.csv
```

### CLI Options

- `--file-type` (required): `tsv`, `gexf`, `cys`
- `--file-location` (required): path to input graph file
- `--nodes`: comma-separated nodes to remove; leave empty to compute centrality without removal
- `--centralities` (required): comma-separated list from `degree`, `unnormalized_degree`, `betweenness`, `closeness`, `eigenvector`, `katz`
- `--output`: output CSV path (default: `centrality_results.csv`)
- `--edge1`: source column name for TSV files (default: `source`)
- `--edge2`: target column name for TSV files (default: `target`)
- `--weight`: weight column name for TSV files (default: `weight`)
- `--network-name`: network name to load from CYS file (default: first network)
- `--directed`: load graph as directed
- `--remove-self-edges`: self-loop removal flag (enabled by default in current CLI implementation)
- `--remove-zero-degree`: remove degree-0 nodes before analysis
- `--largest-component`: analyze only the largest connected component

## Documentation

### 📖 User Guide
- **[Getting Started](docs/wiki/getting-started.md)** - Installation and first steps for GUI and CLI
- **[Workflow Guide](docs/wiki/workflow.md)** - Complete analysis process for GUI and CLI
- **[File Formats](docs/wiki/file-formats.md)** - Supported input formats
- **[Features](docs/wiki/features.md)** - Available analysis options
- **[Examples](docs/wiki/examples.md)** - Sample analyses and use cases

### 🔧 Technical Documentation
- **[Architecture Overview](docs/technical/mvc-architecture.md)** - MVC pattern implementation and CLI execution flow
- **[Models](docs/technical/models.md)** - Data layer and analysis services
- **[Views](docs/technical/views.md)** - GUI components and visualization
- **[Controllers](docs/technical/controllers.md)** - Business logic and event handling
- **[Dependencies](docs/technical/dependencies.md)** - Required libraries
- **[Compilation](docs/technical/compilation.md)** - Building GUI and CLI executables and automated builds

## Workflow Overview

### GUI Workflow
1. **Load Graph**: Select file (TSV/CYS/GEXF) or generate random graph
2. **Configure**: Set column mappings or network selection
3. **Preview**: View graph structure and adjacency list
4. **Select**: Choose nodes to remove and centrality measure
5. **Analyze**: Run analysis to calculate impact on remaining nodes
6. **Visualize**: Explore results in table and graph views
7. **Export**: Save results and visualizations

### CLI Workflow
1. **Load Graph**: Provide `--file-type` and `--file-location`
2. **Configure**: Optional parsing/processing flags for format and graph filtering
3. **Select**: Optional `--nodes` and required `--centralities`
4. **Analyze**: CLI computes centrality impact and diameter deltas
5. **Export**: CSV is written to `--output`

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

This ensures that any modifications, including those used in network services, remain open source.
