from .pydantic import BaseModel, Field
from .users_directories_settings_reply import UsersDirectoriesSettingsReply


class AuthenticationSettingsIdcReply(BaseModel):
    users_directories: UsersDirectoriesSettingsReply = Field(
        alias="users-directories", description="""Users directories."""
    )
