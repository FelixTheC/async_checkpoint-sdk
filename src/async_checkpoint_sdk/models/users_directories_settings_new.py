from .pydantic import BaseModel, Field


class UsersDirectoriesSettingsNew(BaseModel):
    external_user_profile: bool = Field(
        alias="external-user-profile", description="""External user profile."""
    )
    internal_users: bool = Field(alias="internal-users", description="""Internal users.""")
    users_from_external_directories: str = Field(
        alias="users-from-external-directories",
        description="""Users from .external directories.""",
    )
    specific: str | list[str] = Field(
        alias="specific",
        description="""LDAP AU objects identified by the name or UID. Must be set when users-from-external-directories was selected to be specific.""",
    )
