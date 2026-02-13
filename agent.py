"""
Docstring for agent
This module handles asynchronous calls to OpenRouter via MCP.
"""

import os
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Cogni-Agent")

url = "https://openrouter.ai/api/v1/chat/completions"
api_key = os.getenv("OPENROUTER_API_KEY")

@mcp.tool()
async def call_openrouter(prompt: str) -> str:
    if not api_key:
        return "API key not set."

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"
