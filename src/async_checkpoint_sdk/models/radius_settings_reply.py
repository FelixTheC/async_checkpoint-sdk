from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class RadiusSettingsReply(BaseModel):
    server: ApiObjectStandardIdentifier = Field(
        alias="server",
        description="""RADIUS server or RADIUS group object with name and UID.""",
    )
    ask_user_password: bool = Field(
        alias="ask-user-password",
        description="""Ask user for password during authentication.""",
    )
