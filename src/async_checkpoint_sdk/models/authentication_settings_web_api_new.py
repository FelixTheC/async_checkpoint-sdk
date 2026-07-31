from pydantic import BaseModel, Field
from users_directories_settings_new import UsersDirectoriesSettingsNew


class AuthenticationSettingsWebApiNew(BaseModel):
    users_directories: UsersDirectoriesSettingsNew = Field(
        alias="users-directories", description="""Users directories."""
    )
