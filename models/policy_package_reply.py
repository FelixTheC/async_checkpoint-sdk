from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from https_layers_reply import HttpsLayersReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class PolicyPackageReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    access: bool = Field(
        alias="access",
        description="""True - enables, False - disables access policy, empty - nothing is changed.""",
    )
    access_layers: list[dict] = Field(
        alias="access-layers",
        description="""Access policy layers. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    autonomous_threat_policy: str = Field(
        alias="autonomous-threat-policy",
        description="""UID of the Autonomous Threat Prevention policy.""",
    )
    desktop_security: bool = Field(
        alias="desktop-security",
        description="""True - enables, False - disables Desktop security policy, empty - nothing is changed.""",
    )
    https_inspection_layers: HttpsLayersReply = Field(
        alias="https-inspection-layers",
        description="""HTTPS inspection policy layers.""",
    )
    https_inspection_policy: bool = Field(
        alias="https-inspection-policy",
        description="""True - enables, False - disables HTTPS Inspection policy, empty - nothing is changed.""",
    )
    installation_targets: ApiObjectStandardIdentifier = Field(
        alias="installation-targets",
        description="""Which Gateways identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    installation_targets_revision: list[dict] = Field(
        alias="installation-targets-revision",
        description="""List of installation targets and revisions on which this policy package was installed.""",
    )
    nat_layer: str = Field(alias="nat-layer", description="""UID of the NAT policy.""")
    nat_policy: bool = Field(
        alias="nat-policy",
        description="""True - enables, False - disables NAT policy, empty - nothing is changed.""",
    )
    qos: bool = Field(
        alias="qos",
        description="""True - enables, False - disables QoS policy, empty - nothing is changed.""",
    )
    qos_policy_type: str = Field(
        alias="qos-policy-type", description="""QoS policy type."""
    )
    threat_layers: list[dict] = Field(
        alias="threat-layers",
        description="""Threat policy layers. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    threat_prevention: bool = Field(
        alias="threat-prevention",
        description="""True - enables, False - disables Threat policy, empty - nothing is changed.""",
    )
    vpn_traditional_mode: bool = Field(
        alias="vpn-traditional-mode",
        description="""True - enables, False - disables VPN traditional mode, empty - nothing is changed.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
