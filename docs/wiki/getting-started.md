# Getting Started

## Installation

There are three ways to run the application. Try them in order — if one fails, move to the next.

---

### Option 1: Prebuilt Binary

Download the latest release from the [Releases page](../../releases/latest). Choose the file that matches your platform:

| File | Platform |
|---|---|
| `gui-linux` | GUI — Linux |
| `gui-macos` | GUI — macOS |
| `gui-windows.exe` | GUI — Windows |
| `cli-linux` | CLI — Linux |
| `cli-macos` | CLI — macOS |
| `cli-windows.exe` | CLI — Windows |

> **Antivirus warning**: Some antivirus software may flag or block the executable because it is an unsigned binary built with PyInstaller. If this happens, add an exception in your antivirus settings or use Option 2 to compile it yourself.

> **Slow startup**: The first launch of a prebuilt binary may take several seconds while the application unpacks itself. This is normal.

#### Linux — grant execute permission

After downloading, make the file executable before running it:

```bash
chmod +x gui-linux
./gui-linux
```

```bash
chmod +x cli-linux
./cli-linux --help
```

#### macOS — grant execute permission

```bash
chmod +x gui-macos
./gui-macos
```

```bash
chmod +x cli-macos
./cli-macos --help
```

#### Windows

Double-click `gui-windows.exe` to launch the GUI, or run `cli-windows.exe` from a terminal.

---

### Option 2: Compile Your Own Binary

Use this if the prebuilt binary is blocked by your antivirus or does not run on your system.

#### Prerequisites
- Python 3.7 or higher
- pip package manager
- tkinter (see below)

#### Install tkinter

tkinter is not a pip package — it must be installed at the system level.

**Linux (Debian / Ubuntu):**
```bash
sudo apt-get install python3-tk
```

**Linux (Fedora / RHEL):**
```bash
sudo dnf install python3-tkinter
```

**macOS** (if not already included with your Python install):
```bash
brew install python-tk
```

**Windows:** tkinter is bundled with the standard Python installer from [python.org](https://www.python.org/downloads/) — no extra step needed.

#### Create a virtual environment (recommended)

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### Install Python dependencies

```bash
pip install -r requirements.txt
pip install pyinstaller
```

#### Build

**GUI — Linux / macOS:**
```bash
pyinstaller --onefile src/application/main.py \
  --hidden-import=matplotlib.backends.backend_svg \
  --hidden-import=PIL._tkinter_finder \
  --paths=.
```

**GUI — Windows:**
```powershell
pyinstaller --onefile src\application\main.py `
    --hidden-import=matplotlib.backends.backend_svg `
    --hidden-import=PIL._tkinter_finder `
    --paths=.
```

**CLI — Linux / macOS:**
```bash
pyinstaller --onefile src/application/cli.py --paths=.
```

**CLI — Windows:**
```powershell
pyinstaller --onefile src\application\cli.py --paths=.
```

The compiled binary will be placed in the `dist/` folder. On Linux/macOS run `chmod +x dist/<binary>` before executing.

---

### Option 3: Run Directly from Source

Use this if you want to skip compilation entirely and run the application with Python directly.

#### Prerequisites
- Python 3.7 or higher
- pip package manager
- tkinter (see install instructions in Option 2 above)

#### Create a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### Install Python dependencies

```bash
pip install -r requirements.txt
```

#### Run

**GUI:**
```bash
python3 -m src.application.main
```

**CLI:**
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