from pydantic import BaseModel, Field


class WireModeInterfaceReply(BaseModel):
    name: str = Field(alias="name", description="""Interface name.""")
    ip_address: str = Field(alias="ip-address", description="""Interface IP address.""")
    netmask: str = Field(alias="netmask", description="""Interface netmask.""")
