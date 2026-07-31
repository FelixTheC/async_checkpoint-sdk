from pydantic import BaseModel, Field


class DirectTcpSettingsReply(BaseModel):
    ip_address: str = Field(alias="ip-address", description="""Certificate authority IP address.""")
    port: int = Field(alias="port", description="""Port number.""")
