from pydantic import BaseModel, Field


class LeaReply(BaseModel):
    access_permissions: str = Field(
        alias="access-permissions",
        description="""Log reading permissions for the LEA client entity.""",
    )
    administrator_profile: str = Field(
        alias="administrator-profile",
        description="""A profile to set the log reading permissions by for the client entity.""",
    )
    enabled: bool = Field(alias="enabled", description="""N/A""")
