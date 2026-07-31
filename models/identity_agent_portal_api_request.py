from portal_accessibility_request import PortalAccessibilityRequest
from pydantic import BaseModel, Field


class IdentityAgentPortalApiRequest(BaseModel):
    accessibility: PortalAccessibilityRequest = Field(
        alias="accessibility",
        description="""Configuration of the portal access settings.""",
    )
