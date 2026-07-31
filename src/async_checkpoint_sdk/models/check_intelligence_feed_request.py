from intelligence_feed_to_check_request import IntelligenceFeedToCheckRequest
from pydantic import BaseModel, Field


class CheckIntelligenceFeedRequest(BaseModel):
    ioc_feed: IntelligenceFeedToCheckRequest = Field(
        alias="ioc-feed", description="""threat ioc feed parameters."""
    )
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier.""",
    )
