from pydantic import BaseModel, Field


class DirectTcpSettingsRequest(BaseModel):
    ip_address: str = Field(alias="ip-address", description="""Certificate authority IP address.""")
    port: int = Field(alias="port", description="""Port number.""")
