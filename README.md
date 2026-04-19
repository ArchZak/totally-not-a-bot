# TNB Technical Design Document

**Author:** Aarash Zakeri\
**Date:** 04/02/2026\
**Status:** Draft\
**Project:** Totally Not a Bot MCP

Totally not a bot is going to be an MCP to allow agentic AIs to serve as smart enforcement for discord servers alongside server staff

## Problem

### Goals

Want to standardize methods for AI agents to moderate and interact in servers alongside server staff. The idea would be that LLMs can retrieve and analyze message history, send messages, customize profiles, dispense punishment or temporary punishment, etc. Permissions can also be granted to give temporary punishments via silencing. The approach would be designed so that AI agents can regulate multiple servers by setting up oauth passwords via discord bot tokens. So entry to the server will log a bot online, and then make associations with the server. 

### Non-Goals

This approach is based on standardization of security and has nothing to do with the actual AI agent. Methods will be designed to enable MOBILITY across the servers, allow analysis and scraping of channels, and customization of the profile. 

AI agent behavior is independent of the MCP project, so staff preferences, reporting, and other prompt / generation handling is out of the scope of this project. 

## Proposed Solution

### High-Level Approach

A FastMCP server will act as an API to follow the handler -> services. The entry to the server would accept a discord bot token, and then return whether or not a bot exists to actually come online. The implementation of security would have to exist here via password management. 

There will then be implementations of all the relevant methods required for an agent to interact in a server like any normal moderator could. 

So a user would add whatever bot to their server, provide the token to an AI, and then an AI can log into the MCP using that token, where the server would validate that this token actually puts a bot online or not. Security is imperative here. 

### Architecture

Would follow recommended fastmcp structure for entry, tool, resource, prompt directory.

```
tnb_mcp_server/
|-- src/
|   `-- my_server/
|       |-- __init__.py
|       |-- server.py
|       |-- tools/
|       |-- resources/
|       |-- prompts/
|       `-- internals/
|           `-- services/
|-- tests/
|-- pixi.toml
`-- documentation.md
```

### MCP Design

tnb/messages/recent - default fetch 20 messages, or query any num\
tnb/messages/filter - apply any filter like discord search and fetch\
tnb/messages/pins - fetch all pins in channel

tnb/send/message - send text - can optionally reply\
tnb/send/embed - send embed - can optionally reply\
tnb/send/delete - delete its own content\
tnb/send/react - react to messages

tnb/channels - fetch all channels + descriptions + ids in server\
tnb/channels/category - fetch all channels + descriptions + ids in category

tnb/server/emojis - get all emojis\
tnb/server/roles - get all roles + info

tnb/profile/status - set status\
tnb/profile/about - set about me

=============================================

tnb/moderator/silence - mute for 10 mins + reason\
tnb/moderator/mute - mute for any duration + reason\
tnb/moderator/ban - ban + reason\
tnb/moderator/role - assign role\
tnb/moderator/delete - delete messages\
tnb/moderator/dm - dm users

### Blockers

Where should logging be available for users to see?

### Testing Plan


## Alternative Approaches

### Alternative 1
