AEGIS (v1) is an query processing system that combines multiple AI approaches to provide both creative and logical responses to user queries, with refinement capabilities for enhanced output quality.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Overview

AEGIS is designed to process user queries through a sophisticated pipeline that:
1. Classifies queries as either REFLEX or ROUTE and as CREATIVE or LOGIC
2. Generates both creative and logical responses using specialized AI models
3. Refines the responses for improved quality and clarity
4. Stores query history in a local database.

## Architecture

The system follows a modular architecture with distinct layers:
- **Input Layer**: Terminal user interface (entry.py)
- **Classification Layer**: Query type and style classification
- **Processing Layer**: Creative and logical AI response generation
- **Refinement Layer**: Response polishing and enhancement
- **Storage Layer**: Local SQLite database

## Components

### Main Components
- **entry.py**: Terminal user interface that orchestrates the entire system
- **query_handler.py**: Handles query processing and database storage
- **spinal_code.py**: Classification engine using Ollama
- **classifier.py**: Routes queries based on classification
- **receiver.py**: Aggregates responses from creative and logical AIs
- **refinery.py**: Refines responses using OpenRouter API

### AI Modules
- **CREATIVE/creative_ai.py**: Generates creative, imaginative responses
- **LOGIC/logical_ai.py**: Generates logical, analytical responses
- **REFINERY/refinery.py**: Polishes responses using AI refinement

### Supporting Files
- **db.py**: Database operations for storing query history
- **router.py**: Routes queries to appropriate AI modules

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd AEGIS
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure Ollama is installed and running (for query classification):
   - Download from https://ollama.ai
   - Start the service: `ollama serve`

4. Set up API keys (in the respective files):
   - OpenRouter API key for response refinement

## Usage

### Running the System
Start the terminal interface:
```
cd Main_aegis
python entry.py
```

Follow the prompts to enter your queries. The system will:
1. Process your query through the classification system
2. Generate both creative and logical responses
3. Refine the responses for better quality
4. Display all results

### Example Workflow
1. User enters: "Explain quantum computing"
2. System classifies as ROUTE:LOGIC
3. Generates creative and logical explanations
4. Refines both responses
5. Displays original and refined versions

## How It Works

### 1. Query Processing Pipeline
1. User query enters through `entry.py`
2. Query is classified using `spinal_code.py` (requires Ollama)
3. Classification determines processing route
4. Query is stored in local database via `db.py`

### 2. Response Generation
1. `receiver.py` gets the query and sends to both AI modules
2. `creative_ai.py` generates imaginative responses
3. `logical_ai.py` generates analytical responses
4. Both responses are collected by `receiver.py`

### 3. Response Refinement
1. `refinery.py` receives both responses
2. Uses OpenRouter API to refine and polish responses
3. Maintains original meaning while improving clarity
4. Returns refined versions to `entry.py`

### 4. Output Display
1. `entry.py` displays original and refined responses
2. Shows both creative and logical perspectives
3. Formats output for easy comparison

## Project Structure

```
AEGIS/
├── Main_aegis/           # Main application components
│   ├── entry.py          # Terminal user interface
│   ├── query_handler.py  # Query processing and database
│   ├── spinal_code.py    # Classification engine
|   |-- spinal_answer.py  # Answers the query without waking up the whole system (untested)
│   ├── classifier.py     # Query routing logic
│   ├── receiver.py       # Response aggregation
│   ├── db.py             # Database operations
│   └── ...
├── CREATIVE/             # Creative AI module
│   └── creative_ai.py    # Generates creative responses
├── LOGIC/                # Logical AI module
│   └── logical_ai.py     # Generates logical responses
├── REFINERY/             # Response refinement module
│   └── refinery.py       # Refines responses using API
├── requirements.txt      # External dependencies
└── README.txt            # This file
```

## Dependencies

- **Python 3.8+**
- **requests**: For HTTP requests
- **openai**: For AI model integration
- **Ollama**: For local query classification (optional but recommended)
- **SQLite**: Built-in database (no installation needed)

### API Keys Required
- OpenRouter API key for response refinement (hardcoded in files)
- Note: For production, consider using environment variables instead of hardcoded keys

## Configuration

### Environment Variables
For production use, consider setting:
- `OLLAMA_URL`: URL for Ollama service (default: http://localhost:11434/api/generate)
- `OLLAMA_MODEL`: Model name for classification (default: smollm:135m)

### Customization
- Modify classification prompts in `spinal_code.py` and `spinal_codex.py`
- Adjust refinement prompts in `refinery.py`
- Change AI models in the respective AI modules

## Troubleshooting

### Common Issues
- **Ollama not running**: Ensure Ollama service is started before running the system
- **API key errors**: Verify OpenRouter API key is valid and has sufficient credits
- **Network timeouts**: Check internet connectivity for API calls

### Error Handling
- System defaults to ROUTE:LOGIC classification if Ollama is unavailable
- Graceful degradation if refinement API is unreachable
- Database operations include error handling for robustness

## License

[Add license information as appropriate for your project]

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Contact

[Add contact information as appropriate for your project]
