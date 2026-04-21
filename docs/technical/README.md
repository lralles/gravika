# Technical Documentation

This folder contains technical documentation for the Graph Centrality Analysis application.

## Architecture Overview

The application has two execution paths:

- **GUI path** (MVC):
  - **Models** (`src/models/`): Data layer handling graph loading, analysis, and caching
  - **Views** (`src/gui/`): User interface components built with Tkinter
  - **Controllers** (`src/controllers/`): Business logic coordinating between models and views
  - **Application** (`src/application/main.py`): GUI entry point and application setup
- **CLI path**:
  - **Application** (`src/application/cli.py`): Argument parsing, input validation, orchestration, and CSV output
  - **Models** (`src/models/`): Shared graph loading and centrality analysis services used by both GUI and CLI

## Documentation Files

- [MVC Architecture](mvc-architecture.md) - Overview of GUI MVC pattern and CLI execution flow
- [Models](models.md) - Data layer classes and services
- [Views](views.md) - GUI components and user interface
- [Controllers](controllers.md) - Business logic and event handling
- [Dependencies](dependencies.md) - External libraries and requirements
- [Compilation](compilation.md) - Building GUI and CLI executables and automated builds