# region Roles Resources


def get_all_roles():
    pass


def get_role_by_id(role_id: int):
    pass


# endregion

# region Roles Tools


def assign_role_to_user(user_id: int, role_id: int):
    pass


def remove_role_from_user(user_id: int, role_id: int):
    pass


def create_role(name: str, permissions: int):
    pass


def edit_role(role_id: int, name: str = None, permissions: int = None):
    pass


def delete_role(role_id: int):
    pass


def bulk_assign_role_to_users(user_ids: list[int], role_id: int):
    pass


# endregion
