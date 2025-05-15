# server.py
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import json
# Create an MCP server
mcp = FastMCP("curialab")

mock_api_url = "https://68258baf0f0188d7e72d597b.mockapi.io/curia/api/votes"

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def get_votes():
    response = httpx.get(mock_api_url)
    return response.json()

@mcp.tool()
def search_votes(query: str):
    response = httpx.get(mock_api_url, params={"name": query})
    return response.json()

@mcp.tool()
def add_votes(name:str, vp:float):
    response = httpx.post(mock_api_url, json= {"name": name, "vp": vp})
    return response.json()
    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
