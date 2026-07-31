from pydantic import BaseModel, Field


class IcmpOptionsRequest(BaseModel):
    destination: str = Field(
        alias="destination",
        description="""One of these:<br>- Name or UID of an existing object with a unicast IPv4 address (Host, Security Gateway, and so on).<br>- A unicast IPv4 address string (if you do not want to create such an object).""",
    )
    source: str = Field(
        alias="source",
        description="""One of these:<br>- The string main-ip (the probe uses the main IPv4 address of the Security Gateway objects you specified in the parameter [install-on]).<br>- Name or UID of an existing object of type 'Host' with a unicast IPv4 address.<br>- A unicast IPv4 address string (if you do not want to create such an object).""",
    )
