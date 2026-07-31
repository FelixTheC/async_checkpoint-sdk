from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class GatewaysOnboardSettingsReply(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Enable/Disable automatic connection of Security Gateways to Infinity Portal.""",
    )
    connection_method: str = Field(
        alias="connection-method",
        description="""Indicate whether Gateways will be connected to Infinity Portal automatically or only after policy installation.""",
    )
    participant_gateways: str = Field(
        alias="participant-gateways",
        description="""Which Gateways will be connected to Infinity Portal.""",
    )
    specific_gateways: ApiObjectStandardIdentifier = Field(
        alias="specific-gateways",
        description="""Collection of targets identified by Name or UID.""",
    )
