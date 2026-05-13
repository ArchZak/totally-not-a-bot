import asyncio
import os

from config.discord_bot import TotallyNotABot
from dotenv import load_dotenv
from fastmcp import FastMCP
from loguru import logger

mcp = FastMCP("Totally-not-a-Bot")
_client = TotallyNotABot()


async def main():
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN")

    asyncio.create_task(_client.start(token))
    logger.info("Spinning up Discord Bot")

    try:
        logger.info("MCP Server running locally at http://localhost:8000")
        await mcp.run_async(transport="sse")
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        await _client.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
