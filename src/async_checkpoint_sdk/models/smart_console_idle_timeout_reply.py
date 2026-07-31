from .api_domain_identifier import ApiDomainIdentifier
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class SmartConsoleIdleTimeoutReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    enabled: bool = Field(
        alias="enabled",
        description="""Indicates whether to perform logout after being idle.""",
    )
    timeout_duration: int = Field(
        alias="timeout-duration",
        description="""Number of minutes that the SmartConsole will automatically logout after being idle.<br>Updating the interval will take effect only on the next login.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
