from .pydantic import BaseModel, Field


class LeaRequest(BaseModel):
    access_permissions: str = Field(
        alias="access-permissions",
        description="""Log reading permissions for the LEA client entity.""",
    )
    administrator_profile: str = Field(
        alias="administrator-profile",
        description="""A profile to set the log reading permissions by for the client entity.""",
    )
    enabled: bool = Field(
        alias="enabled",
        description="""Whether to enable this client entity on the Opsec Application.""",
    )
