from .api_date_reply import ApiDateReply
from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .lsm_gateway_provisioning_settings_reply import LsmGatewayProvisioningSettingsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field
from .topology_reply import TopologyReply


class LsmGatewayReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    device_id: str = Field(alias="device-id", description="""Device ID.""")
    dynamic_objects: list[dict] = Field(alias="dynamic-objects", description="""Dynamic Objects.""")
    ip_address: str = Field(alias="ip-address", description="""IP address.""")
    os_name: str = Field(alias="os-name", description="""Device platform operating system.""")
    provisioning_settings: LsmGatewayProvisioningSettingsReply = Field(
        alias="provisioning-settings", description="""Provisioning settings."""
    )
    provisioning_state: str = Field(
        alias="provisioning-state", description="""Provisioning state."""
    )
    security_profile: str = Field(alias="security-profile", description="""Attached LSM profile.""")
    sic_name: str = Field(alias="sic-name", description="""Secure Internal Communication name.""")
    sic_state: str = Field(
        alias="sic-state", description="""Secure Internal Communication state."""
    )
    topology: TopologyReply = Field(alias="topology", description="""Topology.""")
    version: str = Field(alias="version", description="""Device platform version.""")
    gateway_status: str = Field(
        alias="gateway-status",
        description="""The current status of the Gateway. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
    last_applied_provisioning_settings_time: ApiDateReply = Field(
        alias="last-applied-provisioning-settings-time",
        description="""The last time when the Provisioning Settings were changed. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
    last_policy_fetch_time: ApiDateReply = Field(
        alias="last-policy-fetch-time",
        description="""The last time when the Security Policy was fetched. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
    last_provisioning_settings_sync_time: ApiDateReply = Field(
        alias="last-provisioning-settings-sync-time",
        description="""The last time of Provisioning Settings synchronization with the Gateway. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
    policy_status: str = Field(
        alias="policy-status",
        description="""The current status of the Security Policy. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
    provisioning_settings_status: str = Field(
        alias="provisioning-settings-status",
        description="""The current status of the Provisioning Settings. Shown only when the 'show-statuses' parameter is set to 'true'.""",
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
