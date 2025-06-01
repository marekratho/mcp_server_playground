# Strava MCP Chatbot

This is a simple Python chatbot that connects to a locally hosted MCP (Model Context Protocol) server. The chatbot acts as an elite cycling coach, analyzing Strava activities and providing interactive, data-driven feedback.

## Features

- Connects to a local MCP server via stdio.
- Uses OpenAI GPT-4o for generating responses.

## Setup

1. **Strava MCP Server**
   - Setup Strava MCP server in accordance with instructions in this [repository](https://github.com/r-huijts/strava-mcp)

2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   - Create a `.env` file in the `src` directory.
   - Add the following params into your `.env`:
     ```
     OPENAI_API_KEY
     MCP_SERVER_PATH=/path/to/your/mcp-server.js
     ```

4. **Run the chatbot:**
   ```sh
   python src/chatbot_agent.py
   ```

## Usage

- When prompted, enter your message or Strava activity details.
- Type `exit` or `quit` to stop the chatbot.

## License

MIT License

---

*This project is for demonstration purposes and is not affiliated with Strava or Mathieu van der Poel.*