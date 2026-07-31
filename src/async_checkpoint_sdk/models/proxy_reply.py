from .pydantic import BaseModel, Field


class ProxyReply(BaseModel):
    address: str = Field(alias="address", description="""N/A""")
    enabled: bool = Field(alias="enabled", description="""N/A""")
    port: str = Field(alias="port", description="""N/A""")
