from .custom_mode_request import CustomModeRequest
from .pydantic import BaseModel, Field


class WebsiteCategorizationRequest(BaseModel):
    mode: str = Field(alias="mode", description="""Website categorization mode.""")
    custom_mode: CustomModeRequest = Field(
        alias="custom-mode", description="""Custom mode object."""
    )
