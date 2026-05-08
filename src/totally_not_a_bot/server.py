from fastmcp import FastMCP

from .resources.category import list_categories

mcp = FastMCP(
    name="Totally-not-a-Bot",
    instructions="An mcp for a discord bot that is definitely not a bot.",
)

mcp.add_resource(list_categories)

if __name__ == "__main__":
    mcp.run()
