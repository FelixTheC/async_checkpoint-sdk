from pydantic import BaseModel, Field


class IfMapServerAuthenticationReply(BaseModel):
    authentication_method: str = Field(
        alias="authentication-method",
        description="""Authentication method for the IF-MAP server.""",
    )
    username: str = Field(
        alias="username", description="""Username for the IF-MAP server authentication."""
    )
