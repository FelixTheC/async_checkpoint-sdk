from .pydantic import BaseModel, Field


class IcmpOptionsRequestNew(BaseModel):
    source: str = Field(
        alias="source",
        description="""One of these:<br>- The string main-ip (the probe uses the main IPv4 address of the Security Gateway objects you specified in the parameter [install-on]).<br>- Name or UID of an existing object of type 'Host' with a unicast IPv4 address.<br>- A unicast IPv4 address string (if you do not want to create such an object).""",
    )
