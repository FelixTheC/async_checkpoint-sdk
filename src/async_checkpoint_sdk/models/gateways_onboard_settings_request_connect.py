from pydantic import BaseModel, Field


class GatewaysOnboardSettingsRequestConnect(BaseModel):
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
    specific_gateways: str | list[str] = Field(
        alias="specific-gateways",
        description="""Selection of targets identified by the name or UID which will be on-boarded to the cloud. Configuration will be applied only when participant-gateways field is set to specific.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
