from network_feed_to_check_request import NetworkFeedToCheckRequest
from pydantic import BaseModel, Field


class CheckNetworkFeedRequest(BaseModel):
    network_feed: NetworkFeedToCheckRequest = Field(
        alias="network-feed", description="""network feed parameters."""
    )
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier.""",
    )
