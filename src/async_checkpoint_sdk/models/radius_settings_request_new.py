from pydantic import BaseModel, Field


class RadiusSettingsRequestNew(BaseModel):
    server: str = Field(
        alias="server",
        description="""RADIUS server or RADIUS group object identified by name or UID.""",
    )
    ask_user_password: bool = Field(
        alias="ask-user-password", description="""Ask user for password during authentication."""
    )
