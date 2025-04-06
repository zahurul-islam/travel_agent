# AI Travel Agency

A comprehensive travel planning application powered by AI agents to help users plan their perfect trip. This application uses multiple specialized AI agents to research destinations, find flights, suggest accommodations, and create detailed itineraries.

## Features

- **Destination Research**: Get detailed information about travel destinations, attractions, local customs, and travel requirements
- **Flight Recommendations**: Search for available flights, compare prices, and find optimal flight choices
- **Accommodation Suggestions**: Find hotels and accommodation based on budget and preferences
- **Itinerary Planning**: Generate detailed day-by-day travel plans incorporating activities, transport, and rest time

## Architecture

The application is built using a multi-agent system with the following components:

- **Research Agent**: Provides information about destinations, attractions, customs, and requirements
- **Flight Agent**: Searches and recommends flight options
- **Hotel Agent**: Finds accommodation options based on user preferences
- **Itinerary Agent**: Creates detailed travel plans and schedules

All agents leverage the Brave Search API to gather real-time information.

## Getting Started

### Prerequisites

- Python 3.7+
- Brave Search API key
- Node.js (for MCP server)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/travel_agent.git
cd travel_agent
```

2. Create and activate a virtual environment
```bash
python -m venv travel
source travel/bin/activate  # On Windows: travel\Scripts\activate
```

3. Install required dependencies
```bash
pip install praisonaiagents rich gradio
```

4. Set up your environment variables
```bash
export BRAVE_API_KEY="your_brave_api_key"  # On Windows: set BRAVE_API_KEY=your_brave_api_key
```

### Running the Application

Start the Gradio web interface:
```bash
python app.py
```

This will launch a local web server, typically at http://127.0.0.1:7860/

## Usage

1. Enter your destination (e.g., "London, UK")
2. Specify your travel dates (e.g., "August 15-22, 2024")
3. Indicate your budget range (e.g., "Mid-range (£1000-£1500)")
4. Share your travel preferences (e.g., "Historical sites, local cuisine, avoiding crowded tourist traps")
5. Click 'Generate Travel Plan'

The system will then generate a comprehensive travel plan including:
- Information about the destination
- Flight recommendations
- Hotel options
- A day-by-day itinerary

## Tech Stack

- **praisonaiagents**: Framework for creating and orchestrating AI agents
- **Gradio**: Web interface for the application
- **Llama 4 (Scout)**: Large Language Model powering the agents
- **Model Context Protocol (MCP)**: For tool integration with Brave Search
- **Brave Search API**: For real-time travel data retrieval

## License

[MIT License](LICENSE)

## Acknowledgments

- Built with [praisonaiagents](https://github.com/praison/praisonaiagents)
- Powered by [Groq](https://groq.com/) for LLM inference
- Search capabilities provided by [Brave Search](https://brave.com/search/)
