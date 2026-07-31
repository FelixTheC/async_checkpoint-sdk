from pydantic import BaseModel, Field


class PrvProfileHostReply(BaseModel):
    host_ip_address: str = Field(alias="host-ip-address", description="""Host IP-Address.""")
    host_name: str = Field(alias="host-name", description="""Host Name.""")
