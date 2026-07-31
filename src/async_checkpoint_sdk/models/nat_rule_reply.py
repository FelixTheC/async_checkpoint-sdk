from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .hits_reply import HitsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class NatRuleReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    auto_generated: bool = Field(alias="auto-generated", description="""N/A""")
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    hits: HitsReply = Field(alias="hits", description="""Hits count object.""")
    install_on: list[dict] = Field(
        alias="install-on",
        description="""Which gateway, identified by the name or UID, to install the policy. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    method: str = Field(alias="method", description="""Nat method.""")
    original_destination: ApiObjectStandardIdentifier = Field(
        alias="original-destination",
        description="""Original destination. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    original_service: ApiObjectStandardIdentifier = Field(
        alias="original-service",
        description="""Original service. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    original_source: ApiObjectStandardIdentifier = Field(
        alias="original-source",
        description="""Original source. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    package: str = Field(alias="package", description="""N/A""")
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    translated_destination: ApiObjectStandardIdentifier = Field(
        alias="translated-destination",
        description="""Translated  destination. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    translated_service: ApiObjectStandardIdentifier = Field(
        alias="translated-service",
        description="""Translated  service. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    translated_source: ApiObjectStandardIdentifier = Field(
        alias="translated-source",
        description="""Translated  source. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
