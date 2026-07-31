from .pydantic import BaseModel, Field


class UsersDirectoriesSettingsReply(BaseModel):
    external_user_profile: bool = Field(alias="external-user-profile", description="""N/A""")
    internal_users: bool = Field(alias="internal-users", description="""N/A""")
    users_from_external_directories: str = Field(
        alias="users-from-external-directories", description="""N/A"""
    )
    specific: list[str] = Field(
        alias="specific",
        description="""LDAP AU objects identified by the name or UID. Must be set when users-from-external-directories was selected to be specific.""",
    )
