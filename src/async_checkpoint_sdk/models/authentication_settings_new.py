from .pydantic import BaseModel, Field
from .users_directories_settings_new import UsersDirectoriesSettingsNew


class AuthenticationSettingsNew(BaseModel):
    authentication_method: str = Field(
        alias="authentication-method", description="""Authentication method."""
    )
    radius: str = Field(
        alias="radius",
        description="""Radius server object identified by the name or UID. Must be set when authentication-method was selected to be radius.""",
    )
    users_directories: UsersDirectoriesSettingsNew = Field(
        alias="users-directories", description="""Users directories."""
    )
