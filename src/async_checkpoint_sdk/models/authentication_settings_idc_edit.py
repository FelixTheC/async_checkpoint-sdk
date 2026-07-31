from .pydantic import BaseModel, Field
from .users_directories_settings_edit import UsersDirectoriesSettingsEdit


class AuthenticationSettingsIdcEdit(BaseModel):
    users_directories: UsersDirectoriesSettingsEdit = Field(
        alias="users-directories", description="""Users directories."""
    )
