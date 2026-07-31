from pydantic import BaseModel, Field


class OtpSettingsReply(BaseModel):
    length: int = Field(alias="length", description="""Length of one time password.""")
    expiration: int = Field(
        alias="expiration", description="""One time password expiration (in minutes)."""
    )
    max_attempts: int = Field(
        alias="max-attempts",
        description="""Number of times users can attempt to enter the one time password before the entire authentication process restarts.""",
    )
