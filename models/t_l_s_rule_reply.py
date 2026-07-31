from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from hits_reply import HitsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class TLSRuleReply(BaseModel):
    name: ApiObjectStandardIdentifier = Field(
        alias="name", description="""HTTPS rule name."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    destination: ApiObjectStandardIdentifier = Field(
        alias="destination",
        description="""Collection of Network objects identified by Name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    service: ApiObjectStandardIdentifier = Field(
        alias="service",
        description="""Collection of Network objects identified by Name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    source: ApiObjectStandardIdentifier = Field(
        alias="source",
        description="""Collection of Network objects identified by Name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    action: ApiObjectStandardIdentifier = Field(
        alias="action", description="""Rule inspect level. Bypass or Inspect."""
    )
    blade: ApiObjectStandardIdentifier = Field(
        alias="blade",
        description="""Blades for HTTPS Inspection. Identified by Name or UID of the blade.""",
    )
    certificate: ApiObjectStandardIdentifier = Field(
        alias="certificate",
        description="""Internal Server Certificate identified by Name or UID,
otherwise, Outbound Certificate is a default value.""",
    )
    destination_negate: bool = Field(
        alias="destination-negate",
        description="""TRUE if negate value is set for Destination.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    hits: HitsReply = Field(alias="hits", description="""Hits count object.""")
    install_on: list[dict] = Field(
        alias="install-on",
        description="""Which gateway, identified by the name or UID, to install the policy. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    layer: ApiObjectStandardIdentifier = Field(
        alias="layer",
        description="""Layer that holds the Object. Identified by the Name or UID.""",
    )
    service_negate: bool = Field(
        alias="service-negate",
        description="""TRUE if negate value is set for Service.""",
    )
    site_category: ApiObjectStandardIdentifier = Field(
        alias="site-category",
        description="""Collection of Network objects identified by Name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    site_category_negate: bool = Field(
        alias="site-category-negate",
        description="""TRUE if negate value is set for Site Category.""",
    )
    source_negate: bool = Field(
        alias="source-negate", description="""TRUE if negate value is set for Source."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    track: ApiObjectStandardIdentifier = Field(
        alias="track",
        description="""None,Log,Alert,Mail,SNMP trap,Mail,User Alert 1, User Alert 2, User Alert 3.""",
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
