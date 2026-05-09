import asyncio
import os

from config.discord_bot import TotallyNotABot
from dotenv import load_dotenv
from fastmcp import FastMCP

# from resources.category import list_categories

mcp = FastMCP(
    name="Totally-not-a-Bot",
    instructions="An mcp for a discord bot that is definitely not a bot.",
)

# mcp.add_resource(list_categories)

client = TotallyNotABot()

load_dotenv()


if __name__ == "__main__":
    asyncio.run(client.run(os.getenv("DISCORD_BOT_TOKEN")))
    mcp.run()
