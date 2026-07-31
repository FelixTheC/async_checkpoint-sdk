from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class AppiStatusReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    last_updated: ApiDateReply = Field(
        alias="last-updated",
        description="""The last time Application Control & URL Filtering was updated on the management server.""",
    )
    installed_version: str = Field(
        alias="installed-version",
        description="""Installed Application Control & URL Filtering version.""",
    )
    installed_version_creation_time: ApiDateReply = Field(
        alias="installed-version-creation-time",
        description="""Installed Application Control & URL Filtering version creation time.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
