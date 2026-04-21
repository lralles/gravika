# Getting Started

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Run the Application

### GUI
```bash
python3 -m src.application.main
```

### CLI
```bash
python3 -m src.application.cli --help
```

## First Launch

### GUI
When you start the GUI application, it automatically loads a random Watts-Strogatz graph with 100 nodes. This allows you to immediately explore the features without needing your own data.

### CLI
The CLI runs one analysis per command and writes output to CSV.

Example:
```bash
python3 -m src.application.cli \
  --file-type tsv \
  --file-location data.tsv \
  --nodes A,B,C \
  --centralities degree,betweenness \
  --output results.csv
```

## CLI Options

- `--file-type` (required): `tsv`, `gexf`, `cys`
- `--file-location` (required): input graph path
- `--nodes`: comma-separated nodes to remove, empty for baseline centrality on all nodes
- `--centralities` (required): `degree`, `unnormalized_degree`, `betweenness`, `closeness`, `eigenvector`, `katz`
- `--output`: output CSV path, default `centrality_results.csv`
- `--edge1`: source column for TSV, default `source`
- `--edge2`: target column for TSV, default `target`
- `--weight`: weight column for TSV, default `weight`
- `--network-name`: network name for CYS, default first network
- `--directed`: load as directed graph
- `--remove-self-edges`: self-loop removal flag (enabled by default in current CLI implementation)
- `--remove-zero-degree`: remove degree-0 nodes before analysis
- `--largest-component`: use only the largest connected component

## Interface Overview (GUI)

The main window contains:

- **Toolbar**: File operations, analysis controls, and options
- **Graph View**: Visual representation of the network
- **Table View**: Analysis results in tabular format
- **Adjacency List**: Text representation of graph structure
- **Status Bar**: Progress updates and current operation status

## Basic Navigation (GUI)

- Use the toolbar buttons to load files or generate random graphs
- Select if you want to remove the zero degree nodes or use the largest component only
- Explore your network on the preview mode
- Select centrality measures from the options
- Use the node selection to choose which nodes to remove
- Click "Run Analysis" to perform the centrality impact analysis

## Getting Help

- CLI: run `python3 -m src.application.cli --help`
- GUI: check the status bar for current operation feedback
- Refer to this documentation for detailed feature explanations