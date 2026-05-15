from typing import Optional

# region Channel Resources


def get_channel_info(channel_id: int):
    pass


def get_all_channels_info():
    pass


def get_channel_activity(channel_id: int):
    pass


def get_inactive_channels():
    pass


# endregion

# region Channel Tools


def create_channel(name: str, channel_type: str, parent_id: Optional[int] = None):
    pass


def edit_channel(
    channel_id: int, new_name: Optional[str] = None, new_parent_id: Optional[int] = None
):
    pass


def delete_channel(channel_id: int):
    pass


def move_channel(channel_id: int, new_parent_id: int):
    pass


# endregion
