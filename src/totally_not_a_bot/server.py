import asyncio
import logging
import os
import sys

from fastmcp import FastMCP

from .config.discord_bot import TotallyNotABot
from .resources.category import list_categories

mcp = FastMCP(
    name="Totally-not-a-Bot",
    instructions="An mcp for a discord bot that is definitely not a bot.",
)

mcp.add_resource(list_categories)

client = TotallyNotABot()


@mcp.on_startup()
async def startup():
    """Starts the discord bot when the MCP server starts."""
    token = os.getenv("DISCORD_BOT_TOKEN")
    if token:
        # thread out the discord bot so it doesn't block the MCP server
        asyncio.create_task(client.run(token))
        logging.info("Discord bot task scheduled.")
    else:
        logging.error("DISCORD_BOT_TOKEN not found in environment variables.")
        sys.exit(1)


if __name__ == "__main__":
    mcp.run()
