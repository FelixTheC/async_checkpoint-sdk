from .pydantic import BaseModel, Field


class CpmiReply(BaseModel):
    administrator_profile: str = Field(
        alias="administrator-profile",
        description="""A profile to set the log reading permissions by for the client entity.""",
    )
    enabled: bool = Field(alias="enabled", description="""N/A""")
    use_administrator_credentials: bool = Field(
        alias="use-administrator-credentials",
        description="""Whether to use the Admin's credentials to login to the security management server.""",
    )
