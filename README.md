# TNB Technical Design Document

**Author:** Aarash Zakeri\
**Date:** 04/24/2026\
**Status:** Draft\
**Project:** Totally Not a Bot MCP

Totally not a bot is going to be an MCP to allow agentic AIs to serve as smart enforcement for discord servers alongside server staff

## Problem

### Goals

Want to standardize methods for AI agents to moderate and interact in servers alongside server staff. The idea would be that LLMs can retrieve and analyze message history, send messages, customize profiles, dispense punishment or temporary punishment, etc. Permissions can also be granted to give temporary punishments via silencing. The approach would be designed so that AI agents can regulate multiple servers by setting up oauth passwords via discord bot tokens. So entry to the server will log a bot online, and then make associations with the server. 

### Non-Goals

This approach is based on standardization of security and has nothing to do with the actual AI agent. Methods will be designed to enable MOBILITY across the servers, allow analysis and scraping of channels, and customization of the profile. 

AI agent behavior is independent of the MCP project, so staff preferences, reporting, and other prompt / generation handling is out of the scope of this project. 

For now, will gear the project towards moderation, and will consider support for bots to act as normal members later once all the tools, prompts, and resources are set up.

## Proposed Solution

### High-Level Approach

A FastMCP server will act as an API to follow the handler -> services. The entry to the server would accept a discord bot token, and then return whether or not a bot exists to actually come online. The implementation of security would have to exist here via password management. The idea would be that multiple AIs can have their own instance of the MCP for their own bot. 

There will then be implementations of all the relevant methods required for an agent to interact in a server like any human moderator could. 

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

#### Auth

tnb/auth/login - login via key
tnb/auth/logout

#### Message Resources

tnb/messages/recent - default fetch 20 messages, or query any num\
tnb/messages/filter - apply any filter like discord search and fetch\
tnb/messages/pins - fetch all pins in channel

#### Message Tools 

tnb/send/message - send text - can optionally reply\
tnb/send/edit - edit text\
tnb/send/embed - send embed - can optionally reply\
tnb/send/delete - delete content\
tnb/send/react - react to messages\
tnb/send/delete_react - remove own reaction from message

#### Channel Resources

tnb/channels - fetch all channels + descriptions + ids in server\
tnb/channels/category - fetch all channels + descriptions + ids in category

#### Channel Tools

tnb/channels/create - create channel\
tnb/channels/edit - edit channel\
tnb/channels/delete - delete channel\
tnb/channels/move - move channel to another category

#### Category Resources

tnb/categories - fetch all categories and their channels

#### Category Tools

tnb/category/create - create category\
tnb/category/edit - edit category\
tnb/category/delete - delete category

#### Profile Resources

tnb/profile/status - set status\
tnb/profile/about - set about me

still deciding whatever down here and where it should go / be organized

#### Role Resources

tnb/roles/get_roles - get all roles + info\
tnb/role/id - get role id

#### Role Tools

tnb/roles/assign_role - assign role\
tnb/roles/remove_role - remove role\
tnb/roles/create_role - create role\
tnb/roles/delete_role - delete role\

#### Enforcement Tools

tnb/enforcement/silence - mute for 10 mins + reason\
tnb/enforcement/mute - mute for any duration + reason\
tnb/enforcement/ban - ban + reason\
tnb/enforcement/kick - kick + reason\
tnb/enforcement/delete - delete messages\
tnb/enforcement/dm - dm users\
tnb/enforcement/rename - rename user\
tnb/enforcement/move - move member between vcs
tnb/enforcement/disconnect - disconnect member from vd


#### General Server Resources

tnb/server/emojis - get all emojis\
tnb/user/id - get user id\


### Blockers

Where should logging be available for users to see?\
Should tnb/messages/recent be based off a time? envisioning a scenario where it grabs the same messages like 50 times cause dead channel\
Should channel creation be seperated per type (voice, forum, etc)?\
TODO: schedule events, invites, emojis, channel override\
What prompts should I add?
Bitmapping stuff across tiers

RN pretty happy with the idea of having channel + tools and then have an entire enforcement column


### Testing Plan

If given to 5 LLMs, they should all act the same. if they dont then the interface is bad

## Alternative Approaches

### Alternative 1
