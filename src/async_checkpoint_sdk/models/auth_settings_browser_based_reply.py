from pydantic import BaseModel, Field
from users_directories_settings_reply import UsersDirectoriesSettingsReply


class AuthSettingsBrowserBasedReply(BaseModel):
    authentication_method: str = Field(
        alias="authentication-method", description="""Authentication method."""
    )
    identity_provider: list[str] = Field(
        alias="identity-provider",
        description="""Identity provider object identified by the name or UID. Must be set when authentication-method was selected to be identity provider.""",
    )
    radius: str = Field(
        alias="radius",
        description="""Radius server object identified by the name or UID. Must be set when authentication-method was selected to be radius.""",
    )
    users_directories: UsersDirectoriesSettingsReply = Field(
        alias="users-directories", description="""Users directories."""
    )
