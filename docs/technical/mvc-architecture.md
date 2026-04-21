# MVC Architecture

The application implements a clean Model-View-Controller architecture for the GUI and a parallel CLI execution flow for non-interactive analysis.

## Architecture Flow

### GUI
```
User Input → View → Controller → Model → Controller → View → User Display
```

### CLI
```
Command Args → CLI Parser/Validator → Model Services → CSV Output + Terminal Summary
```

## Layer Responsibilities

### Model Layer (`src/models/`)
- **Data Management**: Loading graphs from files (TSV, CYS, GEXF)
- **Business Logic**: Centrality analysis and graph processing
- **Caching**: Layout and computation result caching
- **Graph Generation**: Random graph creation

### View Layer (`src/gui/`)
- **User Interface**: Tkinter-based GUI components
- **Data Presentation**: Tables, plots, and interactive elements
- **User Input**: File selection, parameter configuration
- **Visual Feedback**: Status updates and progress indication

### Controller Layer (`src/controllers/`)
- **Event Handling**: Coordinating user actions with business logic
- **Data Flow**: Managing communication between views and models
- **State Management**: Maintaining application state and user preferences

### CLI Application Layer (`src/application/cli.py`)
- **Argument Parsing**: Handles required/optional flags for file input, centralities, filtering, and output
- **Validation**: Checks file existence and centrality names
- **Orchestration**: Loads graph through `GraphLoader`, applies processing filters, and invokes `CentralityAnalysisService.compute`
- **Result Delivery**: Writes CSV output and prints graph stats, diameter before/after, warnings, and preview rows

## Key Design Patterns

- **Dependency Injection**: Controller receives model instances via constructor
- **Observer Pattern**: Views update automatically when data changes
- **Command Pattern**: User actions are encapsulated as controller methods
- **Factory Pattern**: Graph loading supports multiple file formats
- **Shared Service Reuse**: GUI and CLI both consume the same model services for consistent analysis behavior