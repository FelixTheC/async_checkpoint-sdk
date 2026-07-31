from pydantic import BaseModel, Field


class ClientDisplaySettingsReply(BaseModel):
    headline: str = Field(
        alias="headline", description="""Custom headline text for the login screen."""
    )
    username_label: str = Field(
        alias="username-label", description="""Custom label for the username field."""
    )
    password_label: str = Field(
        alias="password-label", description="""Custom label for the password field."""
    )
