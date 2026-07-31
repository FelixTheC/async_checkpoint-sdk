from .pydantic import BaseModel, Field


class AdvancedActionSettingsRequest(BaseModel):
    enable_identity_captive_portal: bool = Field(
        alias="enable-identity-captive-portal", description="""N/A"""
    )
    limit: str = Field(alias="limit", description="""N/A""")
