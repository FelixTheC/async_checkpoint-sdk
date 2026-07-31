from .pydantic import BaseModel, Field


class CloudConnectionRequest(BaseModel):
    community: str = Field(alias="community", description="""N/A""")
    endpoints: list[str] = Field(alias="endpoints", description="""N/A""")
    gateway: str = Field(alias="gateway", description="""N/A""")
    supported_encryption_settings: str = Field(
        alias="supported-encryption-settings", description="""N/A"""
    )
