from .pydantic import BaseModel, Field


class InternalAccessRequest(BaseModel):
    undefined: bool = Field(
        alias="undefined",
        description="""Controls portal access settings for internal interfaces, whose topology is set to 'Undefined'.""",
    )
    dmz: bool = Field(
        alias="dmz",
        description="""Controls portal access settings for internal interfaces, whose topology is set to 'DMZ'.""",
    )
    vpn: bool = Field(
        alias="vpn",
        description="""Controls portal access settings for interfaces that are part of a VPN Encryption Domain.""",
    )
