from praisonaiagents import Agent, Agents, MCP
import os
from rich import print
import gradio as gr

brave_api_key = os.getenv("BRAVE_API_KEY")

# Travel Research Agent
research_agent = Agent(
    instructions="Research about travel destinations, attractions, local customs, and travel requirements",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npx -y @modelcontextprotocol/server-brave-search", env={"BRAVE_API_KEY": brave_api_key})
)

# Flight Booking Agent
flight_agent = Agent(
    instructions="Search for available flights, compare prices, and recommend optimal flight choices",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npx -y @modelcontextprotocol/server-brave-search", env={"BRAVE_API_KEY": brave_api_key})
)

# Accommodation Agent
hotel_agent = Agent(
    instructions="Research hotels and accommodation based on budget and preferences",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npx -y @modelcontextprotocol/server-brave-search", env={"BRAVE_API_KEY": brave_api_key})
)

# Itinerary Planning Agent
itinerary_agent = Agent(
    instructions="Design detailed day-by-day travel plans incorporating activities, transport, and rest time",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npx -y @modelcontextprotocol/server-brave-search", env={"BRAVE_API_KEY": brave_api_key})
)

def generate_travel_plan(destination, dates, budget, preferences):
    """Generate a travel plan using the AI agents"""
    
    # Create the travel query
    travel_query = f"""Create a comprehensive travel plan for {destination} during {dates}.
    Budget: {budget}
    Preferences: {preferences}
    
    Include:
    1. Information about the destination
    2. Flight recommendations
    3. Hotel options
    4. A day-by-day itinerary
    """
    
    # Initialize the agents team
    agents = Agents(agents=[research_agent, flight_agent, hotel_agent, itinerary_agent])
    
    try:
        # Generate the travel plan
        result = agents.start(travel_query)
        
        # Format the output
        formatted_result = f"""
=== TRAVEL PLAN: {destination} ===

Dates: {dates}
Budget: {budget}
Preferences: {preferences}

{result}
"""
        
        return formatted_result
    except Exception as e:
        return f"Error generating travel plan: {str(e)}"

# Create the Gradio interface
with gr.Blocks(title="AI Travel Agency", theme="soft") as demo:
    gr.Markdown("# 🌍 AI Travel Agency")
    gr.Markdown("Plan your perfect trip with our AI agents")
    
    with gr.Row():
        with gr.Column(scale=1):
            destination = gr.Textbox(label="Destination", placeholder="London, UK", value="London, UK")
            dates = gr.Textbox(label="Travel Dates", placeholder="August 15-22, 2024", value="August 15-22, 2024")
            budget = gr.Textbox(label="Budget", placeholder="Mid-range (£1000-£1500)", value="Mid-range (£1000-£1500)")
            preferences = gr.Textbox(
                label="Travel Preferences", 
                placeholder="Historical sites, local cuisine, avoiding crowded tourist traps",
                value="Historical sites, local cuisine, avoiding crowded tourist traps"
            )
            submit_btn = gr.Button("Generate Travel Plan 🚀", variant="primary")
        
        with gr.Column(scale=2):
            output = gr.Markdown(label="Your Travel Plan")
    
    submit_btn.click(
        generate_travel_plan,
        inputs=[destination, dates, budget, preferences],
        outputs=output
    )
    
    gr.Markdown("### How to use")
    gr.Markdown("""
    1. Enter your destination
    2. Specify your travel dates
    3. Indicate your budget range
    4. Share your travel preferences
    5. Click 'Generate Travel Plan'
    
    *Note: Generation may take a minute or two as our AI agents research your perfect trip.*
    """)

# Run the CLI version when script is run directly
if __name__ == "__main__":
    # Launch the Gradio interface
    demo.launch()
    
    # Example CLI usage (commented out when using Gradio)
    """
    destination = "London, UK"
    dates = "August 15-22, 2025"
    budget = "Mid-range (£1000-£1500)"
    preferences = "Historical sites, local cuisine, avoiding crowded tourist traps"
    
    travel_query = f"What are the best attractions to visit in {destination} during {dates} on a budget of {budget} with preferences of {preferences}?"
    agents = Agents(agents=[planning_agent, flight_agent, hotel_agent, planning_agent])
    result = agents.start(travel_query)
    print(f"\n=== DESTINATION RESEARCH: {destination} ===\n")
    print(result)
    """
F
