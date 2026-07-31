from pydantic import BaseModel, Field


class SslNetworkExtenderRequest(BaseModel):
    ssl_enable: bool = Field(alias="ssl-enable", description="""N/A""")
