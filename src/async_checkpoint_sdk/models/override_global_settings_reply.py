from .pydantic import BaseModel, Field
from .website_categorization_reply import WebsiteCategorizationReply


class OverrideGlobalSettingsReply(BaseModel):
    fail_mode: str = Field(
        alias="fail-mode", description="""Fail mode - allow or block all requests."""
    )
    website_categorization: WebsiteCategorizationReply = Field(
        alias="website-categorization", description="""Website categorization object."""
    )
