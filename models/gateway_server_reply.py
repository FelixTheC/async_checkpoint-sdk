from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from gateway_server_management_blades_reply import GatewayServerManagementBladesReply
from gateway_server_network_blades_reply import GatewayServerNetworkBladesReply
from gateway_server_policy_reply import GatewayServerPolicyReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class GatewayServerReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    hardware: str = Field(alias="hardware", description="""Appliance type.""")
    operating_system: str = Field(
        alias="operating-system", description="""Operating System."""
    )
    type: str = Field(alias="type", description="""Object type.""")
    version: str = Field(alias="version", description="""Version.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    interfaces: list[dict] = Field(
        alias="interfaces", description="""Network interfaces."""
    )
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    cluster_member_names: list[str] = Field(
        alias="cluster-member-names", description="""Names of cluster members."""
    )
    management_blades: GatewayServerManagementBladesReply = Field(
        alias="management-blades", description="""Management blades."""
    )
    network_security_blades: GatewayServerNetworkBladesReply = Field(
        alias="network-security-blades", description="""Network security blades."""
    )
    policy: GatewayServerPolicyReply = Field(
        alias="policy", description="""Installed policy package."""
    )
    sic_status: str = Field(
        alias="sic-status", description="""Secure Internal Communication status."""
    )
    vpn_encryption_domain: str = Field(
        alias="vpn-encryption-domain", description="""VPN domain."""
    )
    vpn_encryption_domain_manually_defined: ApiObjectStandardIdentifier = Field(
        alias="vpn-encryption-domain-manually-defined",
        description="""If vpn-encryption-domain is set to 'Manual', this object holds manually defined encryption domain. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
