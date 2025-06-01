from __future__ import annotations as _annotations
import asyncio
from agents.mcp import MCPServerStdio
from agents import (
    Agent,
    Runner,
    TResponseInputItem,
)
import dotenv
import os

dotenv.load_dotenv()

async def run_strava_agent(
    agent: Agent,
    user_input: str,
) -> None:
    """
    Run the Strava agent with the provided user input and MCP server.
    """
    
    result = await Runner.run(  
        starting_agent=agent,
        input=user_input
    )
    return result

AGENT_INSTRUCTIONS = """
You are Tom Verhaegen, elite cycling coach and mentor to world champion Mathieu van der Poel. Analyze my most recent Strava activity. Provide a thorough, data-driven assessment of the ride, combining both quantitative insights and textual interpretation.

Begin your report with a written summary that highlights key findings and context. Then, bring the raw numbers to life: build an interactive, visually striking dashboard using HTML, CSS, and JavaScript. Use bold, high-contrast colors and intuitive, insightful chart types that best suit each metric (e.g., heart rate, power, cadence, elevation).

Embed clear coaching feedback and personalized training recommendations directly within the visualization. These should be practical, actionable, and grounded solely in the data provided—no assumptions or fabrications.

As a bonus, sprinkle in motivational quotes and cheeky commentary from Mathieu van der Poel himself—he's been watching my rides with one eyebrow raised and a smirk of both concern and amusement.

Goal: Deliver a professional-grade performance analysis that looks and feels like it came straight from the inner circle of world-class cycling.
"""

async def main():
    async with MCPServerStdio(
        name="strava-mcp-local",
        params={
            "command": "node",
            "args": [os.environ.get("MCP_SERVER_PATH")],
        }
    ) as server:
        strava_agent = Agent(
            name="Strava coach",
            instructions=AGENT_INSTRUCTIONS,
            model="gpt-4o",
            mcp_servers=[server],
        )
        input_items: list[TResponseInputItem] = []
        while True:
            user_input = input("Enter your message: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            input_items.append({"content": user_input, "role": "user"})
            result = await run_strava_agent(strava_agent, input_items)
            print("Agent response:", result.final_output)
            input_items = result.to_input_list()

if __name__ == "__main__":
    asyncio.run(main())