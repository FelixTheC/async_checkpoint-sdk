from .pydantic import BaseModel, Field
from .website_categorization_request import WebsiteCategorizationRequest


class OverrideGlobalSettingsRequest(BaseModel):
    fail_mode: str = Field(
        alias="fail-mode", description="""Fail mode - allow or block all requests."""
    )
    website_categorization: WebsiteCategorizationRequest = Field(
        alias="website-categorization", description="""Website categorization object."""
    )
