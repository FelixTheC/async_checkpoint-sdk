from pydantic import BaseModel, Field


class ClientDisplaySettingsRequest(BaseModel):
    headline: str = Field(
        alias="headline", description="""Display headline for authentication dialog."""
    )
    username_label: str = Field(alias="username-label", description="""Label for username field.""")
    password_label: str = Field(alias="password-label", description="""Label for password field.""")
