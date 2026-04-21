# Compilation Guide

This guide covers building standalone executables for the Graph Centrality Analysis application.

## Run From Source

### GUI
```bash
python3 -m src.application.main
```

### CLI
```bash
python3 -m src.application.cli --help
```

Example:
```bash
python3 -m src.application.cli \
  --file-type tsv \
  --file-location data.tsv \
  --nodes A,B,C \
  --centralities degree,betweenness \
  --output results.csv
```

## Manual Compilation

### Prerequisites
- Python 3.7+ installed
- All dependencies from `requirements.txt`
- PyInstaller package

### Install Build Dependencies
```bash
pip install -r requirements.txt
pip install pyinstaller
```

### Build Executable

#### GUI: Linux/macOS
```bash
pyinstaller --onefile src/application/main.py \
  --hidden-import=matplotlib.backends.backend_svg \
  --hidden-import=PIL._tkinter_finder \
  --paths=.
```

#### GUI: Windows
```cmd
pyinstaller --onefile src\application\main.py ^
  --hidden-import=matplotlib.backends.backend_svg ^
  --hidden-import=PIL._tkinter_finder ^
  --paths=.
```

#### CLI: Linux/macOS
```bash
pyinstaller --onefile src/application/cli.py \
  --paths=.
```

#### CLI: Windows
```cmd
pyinstaller --onefile src\application\cli.py ^
  --paths=.
```

### PyInstaller Options Explained
- `--onefile`: Creates a single executable file
- `--hidden-import=matplotlib.backends.backend_svg`: Includes SVG backend for matplotlib (GUI builds)
- `--hidden-import=PIL._tkinter_finder`: Ensures PIL/Pillow works with Tkinter (GUI builds)
- `--paths=.`: Adds current directory to Python path for imports

### Run Compiled Executable

#### GUI Linux/macOS
```bash
chmod +x dist/main
./dist/main
```

#### GUI Windows
```cmd
dist\main.exe
```

#### CLI Linux/macOS
```bash
chmod +x dist/cli
./dist/cli --help
```

#### CLI Windows
```cmd
dist\cli.exe --help
```

## Automated Builds (GitHub Actions)

The repository includes automated build workflows that create executables for both Linux and Windows platforms.

### Workflow Files
- `.github/workflows/release-gui-linux.yml` - GUI Linux builds
- `.github/workflows/release-gui-windows.yml` - GUI Windows builds
- `.github/workflows/release-cli-linux.yml` - CLI Linux builds and release
- `.github/workflows/release-cli-windows.yml` - CLI Windows builds and release

### Build Process
1. **Trigger**: Automatically runs on pushes to `main` branch
2. **Environment**: Uses Python 3.11 on respective OS runners
3. **Dependencies**: Installs requirements and PyInstaller
4. **Build**: Creates platform-specific executables
5. **Release**: Publishes executables as GitHub releases

### CLI Artifact Names
- Linux artifact: `cli-linux`
- Windows artifact: `cli-windows.exe`

