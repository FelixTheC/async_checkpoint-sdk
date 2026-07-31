from .pydantic import BaseModel, Field


class LsmClusterMemberInterfacesReply(BaseModel):
    ip_address: str = Field(alias="ip-address", description="""IP address.""")
    name: str = Field(alias="name", description="""Interface name.""")
