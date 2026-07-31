from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class MdPermissionsProfileReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    permission_level: str = Field(
        alias="permission-level",
        description="""The level of the Multi Domain Permissions Profile.<br>The level cannot be changed after creation.""",
    )
    mds_provisioning: bool = Field(
        alias="mds-provisioning",
        description="""Create and manage Multi-Domain Servers and Multi-Domain Log Servers.<br>Only a Super User permission-level profile can select this option.""",
    )
    manage_all_domains: bool = Field(
        alias="manage-all-domains",
        description="""Create and manage all Domains and Global Domains.""",
    )
    manage_admins: bool = Field(
        alias="manage-admins",
        description="""Create and manage Multi-Domain Security Management administrators with the same or lower permission level. For example, a Domain manager cannot create Superusers or global managers.<br>Only a 'Manager' permission-level profile can edit this permission.""",
    )
    manage_sessions: bool = Field(
        alias="manage-sessions",
        description="""Connect/disconnect Domain sessions, publish changes, and delete other administrator sessions.<br>Only a 'Manager' permission-level profile can edit this permission.""",
    )
    management_api_login: bool = Field(
        alias="management-api-login",
        description="""Permission to log in to the Security Management Server and run API commands using these tools: mgmt_cli (Linux and Windows binaries), Gaia CLI (clish) and Web Services (REST). Useful if you want to prevent administrators from running automatic scripts on the Management.<br>Note: This permission is not required to run commands from within the API terminal in SmartConsole.""",
    )
    cme_operations: str = Field(
        alias="cme-operations",
        description="""Permission to read / edit the Cloud Management Extension (CME) configuration.""",
    )
    global_vpn_management: bool = Field(
        alias="global-vpn-management",
        description="""Lets the administrator select Enable global use for a Security Gateway shown in the MDS Gateways & Servers view.<br>Only a 'Manager' permission-level profile can edit this permission.""",
    )
    manage_global_assignments: bool = Field(
        alias="manage-global-assignments",
        description="""Controls the ability to create, edit and delete global assignment and not the ability to reassign, which is set according to the specific Domain's permission profile.""",
    )
    enable_default_profile_for_global_domains: bool = Field(
        alias="enable-default-profile-for-global-domains",
        description="""Enable the option to specify a default profile for all global domains.""",
    )
    default_profile_global_domains: ApiObjectStandardIdentifier = Field(
        alias="default-profile-global-domains",
        description="""The default profile for all global domains.""",
    )
    view_global_objects_in_domain: bool = Field(
        alias="view-global-objects-in-domain",
        description="""Lets an administrator with no global objects permissions view the global objects in the domain. This option is required for valid domain management.""",
    )
    enable_default_profile_for_local_domains: bool = Field(
        alias="enable-default-profile-for-local-domains",
        description="""Enable the option to specify a default profile for all local domains.""",
    )
    default_profile_local_domains: ApiObjectStandardIdentifier = Field(
        alias="default-profile-local-domains",
        description="""The default profile for all local domains.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
