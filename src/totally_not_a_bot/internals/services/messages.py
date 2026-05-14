from datetime import datetime
from typing import Annotated, Optional

from config.models import Message

# region Message Resources


def get_recent_messages(
    channel_id: int,
    limit: int = 20,
    timestamp: Annotated[Optional[datetime], "Filter messages newer than this"] = None,
) -> list[Message]:
    """
    Fetch recent messages from a specific channel and filtered by a given timestamp, or default to the last 30 minutes worth of messages that fit the limit.

    Args:
        channel_id (int): The ID of the channel to fetch messages from.
        limit (int, optional): The maximum number of messages to fetch. Defaults to 20.
        timestamp (datetime, optional): Filter messages newer than this timestamp. Defaults to None.

    Returns:
        list[Message]: A list of Message objects representing the recent messages in the channel.
    """
    pass


def get_messages_by_filter():
    pass


def get_pinned_messages():
    pass


def get_messages_in_context_window():
    pass


def get_threads_to_message():
    pass


def get_message_states():
    pass


# endregion

# region Message Tools


def send_message(
    channel_id: int, content: str, reply_to_message_id: Optional[int] = None
):
    pass


def edit_message(message_id: int, new_content: str):
    pass


def send_embed(
    channel_id: int, embed_data: dict, reply_to_message_id: Optional[int] = None
):
    pass


def edit_embed(message_id: int, new_embed_data: dict):
    pass


def delete_message(message_id: int):
    pass


def add_reaction(message_id: int, emoji: str):
    pass


def remove_reaction(message_id: int, emoji: str):
    pass


def delete_messages(message_ids: list[int]):
    pass


def pin_message(message_id: int):
    pass


def unpin_message(message_id: int):
    pass


# endregion
