from .add import add
from .pydantic import BaseModel, Field
from .remove import remove
from .users_directories_settings_edit import UsersDirectoriesSettingsEdit


class AuthSettingsBrowserBasedEdit(BaseModel):
    authentication_method: str = Field(
        alias="authentication-method", description="""Authentication method."""
    )
    identity_provider: add | remove | str | list[str] = Field(
        alias="identity-provider",
        description="""Identity provider object identified by the name or UID. Must be set when authentication-method was selected to be identity provider.""",
    )
    radius: str = Field(
        alias="radius",
        description="""Radius server object identified by the name or UID. Must be set when authentication-method was selected to be radius.""",
    )
    users_directories: UsersDirectoriesSettingsEdit = Field(
        alias="users-directories", description="""Users directories."""
    )
