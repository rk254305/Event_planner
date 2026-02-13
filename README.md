<<<<<<< HEAD
# Event_planner
Event Planner AI using RAG, LangChain Agents, FAISS vector search, and Ollama LLM with Streamlit UI.
=======
# Event Planning AI Program

This program uses an open-source Large Language Model (LLM) via Ollama to assist with event planning tasks.

## Features

- **Event Plan Generation**: Create detailed event plans including venue suggestions, themes, menus, entertainment, timelines, and budget breakdowns.
- **Social Media Post Creation**: Generate engaging social media posts to promote events.
- **Personalized Recommendations**: Provide tailored event ideas based on user profiles.

## Prerequisites

- Python 3.7+
- Ollama installed and running with Llama2 model
  - Install Ollama: https://ollama.ai/
  - Pull Llama2: `ollama pull llama2`

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the program from the command line with appropriate arguments:

### Generate an Event Plan
```
python event_planner.py --task plan --event_type wedding --guests 100 --budget "$50,000" --preferences "outdoor, elegant, vegetarian options"
```

### Create a Social Media Post
```
python event_planner.py --task post --event_type birthday --date "2024-05-15"
```

### Get Personalized Recommendations
```
python event_planner.py --task personalize --profile "Enjoys outdoor activities, prefers casual events, allergic to nuts" --event_type corporate
```

## How It Works

The program uses LangChain's OllamaLLM integration to interact with the Llama2 model running locally via Ollama. It constructs prompts based on user input and generates relevant content for event planning.

## Example Output

For an event plan request:
```
Event Plan:
Based on your wedding for 100 guests with a $50,000 budget and preferences for outdoor, elegant, vegetarian options...

1. Venue suggestions: Botanical gardens, beachfront resorts, or elegant outdoor pavilions...
[Full detailed plan follows]
```

## Contributing

Feel free to contribute by adding more features or improving the prompts for better results.
>>>>>>> 27c8fcc (Initial commit with Event Planner AI (RAG + Agents))
