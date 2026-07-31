from custom_mode_reply import CustomModeReply
from pydantic import BaseModel, Field


class WebsiteCategorizationReply(BaseModel):
    mode: str = Field(alias="mode", description="""Website categorization mode.""")
    custom_mode: CustomModeReply = Field(alias="custom-mode", description="""Custom mode object.""")
