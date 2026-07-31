from api_date_reply import ApiDateReply
from lsm_cluster_member_provisioning_settings_reply import (
    LsmClusterMemberProvisioningSettingsReply,
)
from pydantic import BaseModel, Field


class LsmClusterMemberReply(BaseModel):
    member_name: str = Field(
        alias="member-name",
        description="""Member name. Consists of the member name in the LSM profile and the prefix or suffix of the cluster.""",
    )
    member_uid: str = Field(alias="member-uid", description="""Member uid.""")
    device_id: str = Field(alias="device-id", description="""Device ID.""")
    interfaces: list[dict] = Field(alias="interfaces", description="""Interfaces.""")
    main_ip_address: str = Field(
        alias="main-ip-address", description="""Main ip address."""
    )
    provisioning_settings: LsmClusterMemberProvisioningSettingsReply = Field(
        alias="provisioning-settings", description="""Provisioning settings."""
    )
    provisioning_state: str = Field(
        alias="provisioning-state", description="""Provisioning state."""
    )
    sic_name: str = Field(
        alias="sic-name", description="""Secure Internal Communication name."""
    )
    sic_state: str = Field(
        alias="sic-state", description="""Secure Internal Communication state."""
    )
    gateway_status: str = Field(
        alias="gateway-status",
        description="""The current status of the Cluster member. Shown only when the 'show-statuses' parameter is set to 'true'.""",
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
        description="""The last time of Provisioning Settings synchronization with the Cluster member. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
    policy_status: str = Field(
        alias="policy-status",
        description="""The current status of the Security Policy. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
    provisioning_settings_status: str = Field(
        alias="provisioning-settings-status",
        description="""The current status of the Provisioning Settings. Shown only when the 'show-statuses' parameter is set to 'true'.""",
    )
