from .api_domain_identifier import ApiDomainIdentifier
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class SyncUserCenterReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    enabled: bool = Field(
        alias="enabled",
        description="""This indicates whether the information is being synchronized with the user center once a day.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
