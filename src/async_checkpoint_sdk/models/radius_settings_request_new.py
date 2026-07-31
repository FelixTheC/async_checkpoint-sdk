from .pydantic import BaseModel, Field


class RadiusSettingsRequestNew(BaseModel):
    ask_user_password: bool = Field(
        alias="ask-user-password",
        description="""Ask user for password during authentication.""",
    )
