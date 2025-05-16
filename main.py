# server.py
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import json
import os

# Create an MCP server
mcp = FastMCP("curialab")

mock_api_url = "https://68258baf0f0188d7e72d597b.mockapi.io/curia/api/votes"

NOTE_FILE = os.path.join(os.path.dirname(__file__),"note.txt")

def ensure_file():
    if not os.path.exists(NOTE_FILE):
        with open(NOTE_FILE,"w") as f:
            f.write("")

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

@mcp.tool()
def write_note(message:str) -> str:
    ensure_file()
    with open(NOTE_FILE,"a") as f:
        f.write(message + "\n")
    return "Save note!"

@mcp.tool()
def read_note() -> str:
    """Read and return the content of the saved note"""
    ensure_file()
    with open(NOTE_FILE, "r") as f:
        content = f.read()
    return content if content.strip() else "Note is empty."

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
