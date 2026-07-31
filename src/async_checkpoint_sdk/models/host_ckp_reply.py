from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .host_ckp_log_settings_reply import HostCkpLogSettingsReply
from .host_ckp_management_blades_reply import HostCkpManagementBladesReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field
from .third_party_nat_reply import ThirdPartyNatReply


class HostCkpReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    interfaces: list[dict] = Field(
        alias="interfaces", description="""Check Point host interfaces."""
    )
    ipv4_address: str = Field(alias="ipv4-address", description="""IPv4 address.""")
    ipv6_address: str = Field(alias="ipv6-address", description="""IPv6 address.""")
    nat_settings: ThirdPartyNatReply = Field(alias="nat-settings", description="""NAT settings.""")
    type: str = Field(alias="type", description="""Object type.""")
    firewall: bool = Field(alias="firewall", description="""Firewall blade enabled.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    hardware: str = Field(alias="hardware", description="""Hardware name.""")
    os: str = Field(alias="os", description="""Operating system name.""")
    sic_name: str = Field(alias="sic-name", description="""Secure Internal Connection name.""")
    sic_state: str = Field(
        alias="sic-state", description="""Secure Internal Connection trust state."""
    )
    version: str = Field(alias="version", description="""Check Point host platform version.""")
    management_blades: HostCkpManagementBladesReply = Field(
        alias="management-blades", description="""Management blades."""
    )
    logs_settings: HostCkpLogSettingsReply = Field(
        alias="logs-settings", description="""Logs settings."""
    )
    save_logs_locally: bool = Field(
        alias="save-logs-locally", description="""Save logs locally enabled."""
    )
    send_alerts_to_server: list[dict] = Field(
        alias="send-alerts-to-server",
        description="""Collection of Server(s) to send alerts to identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    send_logs_to_backup_server: list[dict] = Field(
        alias="send-logs-to-backup-server",
        description="""Collection of Backup server(s) to send logs to identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    send_logs_to_server: list[dict] = Field(
        alias="send-logs-to-server",
        description="""Collection of Servers(s) to send logs to identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
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
