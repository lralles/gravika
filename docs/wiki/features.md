# Features

The Graph Centrality Analysis application provides comprehensive tools for analyzing network structure and node importance through both GUI and CLI interfaces.

## Interface Modes

### GUI
- Interactive visualization and exploratory analysis
- Random graph generation support
- Table and graph views for results
- Export to CSV, SVG, and CYS

### CLI
- Batch-friendly command execution
- Fast non-interactive analysis for larger graphs
- CSV export with terminal summary
- Compatible with scripts and automation

## Graph Loading

### File Support
- **TSV/CSV**: Tab or comma-separated edge lists
- **CYS**: Cytoscape session files with multiple networks
- **GEXF**: Standard graph exchange format

### Random Graph Generation
- **GUI only**
- **Erdős-Rényi**: Random graphs with fixed edge probability
- **Barabási-Albert**: Scale-free networks with preferential attachment
- **Watts-Strogatz**: Small-world networks with clustering

## Graph Processing

### Filtering Options
- **Zero-Degree Removal**: Exclude isolated nodes from analysis (`--remove-zero-degree` in CLI)
- **Largest Component**: Focus on main connected component (`--largest-component` in CLI)
- **Self-Edge Removal**: Self-loop removal is enabled by default in current CLI implementation (`--remove-self-edges`) and configurable in GUI

### Graph Types
- **Directed**: Preserves edge direction (`--directed` in CLI)
- **Undirected**: Treats all edges as bidirectional

## Centrality Measures

### Available Metrics
- **Degree Centrality (Unnormalized)**: Number of direct connections
- **Degree Centrality (Normalized)**: Number of direct connections / Total number of Connections
- **Betweenness Centrality**: Importance as network bridge
- **Closeness Centrality**: Average distance to all nodes
- **Eigenvector Centrality**: Influence based on neighbor importance
- **Katz Centrality**: Weighted sum of path lengths

### Analysis Features
- **Node Removal Impact**: Calculate centrality changes after removing specific nodes
- **Comparative Analysis**: Before/after centrality values
- **Impact Ranking**: Sort nodes by centrality change magnitude
- **Diameter Comparison**: Reports graph diameter before and after removal

## Visualization

### Graph Display
- **GUI only**
- **Node Coloring**: Visual representation of impact (red=increase, blue=decrease)
- **Edge Styling**: Thickness based on weights or impact
- **Layout Algorithms**: Automatic positioning for clear visualization
- **Removed Node Marking**: Highlight nodes selected for removal

### Display Options
- **GUI only**
- **Node Labels**: Show/hide node names
- **Edge Highlighting**: Emphasize affected connections

## Data Views

### Table View
- **GUI**: Sortable interactive table with impact values
- **CLI**: CSV output with full per-node result table

### Adjacency List
- **GUI only**
- **Text Representation**: Complete graph structure as text
- **Connection Details**: Shows all node relationships
- **Debugging Aid**: Verify graph loading accuracy

## Export Capabilities

### Result Formats
- **GUI**: CSV, SVG, CYS
- **CLI**: CSV
