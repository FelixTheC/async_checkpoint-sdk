from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field
from .threat_rule_track_settings_reply import ThreatRuleTrackSettingsReply


class ThreatRuleReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    action: ApiObjectStandardIdentifier = Field(
        alias="action",
        description="""Action-the enforced profile. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    destination: list[dict] = Field(
        alias="destination",
        description="""Collection of Network objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    destination_negate: bool = Field(
        alias="destination-negate",
        description="""True if negate is set for destination.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    exceptions: ApiObjectStandardIdentifier = Field(
        alias="exceptions", description="""The rule's exceptions."""
    )
    exceptions_layer: str = Field(
        alias="exceptions-layer", description="""The rule's exceptions layer."""
    )
    install_on: list[dict] = Field(
        alias="install-on",
        description="""Which gateway, identified by the name or UID, to install the policy. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    layer: str = Field(alias="layer", description="""N/A""")
    protected_scope: list[dict] = Field(
        alias="protected-scope",
        description="""Collection of network objects defining Protection Scope identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    protected_scope_negate: bool = Field(
        alias="protected-scope-negate",
        description="""True if negate is set for Protected Scope.""",
    )
    service: list[dict] = Field(
        alias="service",
        description="""Collection of network objects defining Service identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    service_negate: bool = Field(
        alias="service-negate", description="""True if negate is set for Service."""
    )
    source: list[dict] = Field(
        alias="source",
        description="""Collection of network objects defining Source identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    source_negate: bool = Field(
        alias="source-negate", description="""True if negate is set for source."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    track: ApiObjectStandardIdentifier = Field(
        alias="track",
        description="""Packet tracking. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    track_settings: ThreatRuleTrackSettingsReply = Field(
        alias="track-settings", description="""Threat rule track settings."""
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
