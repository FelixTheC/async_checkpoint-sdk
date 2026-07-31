from .pydantic import BaseModel, Field


class MdPermissionsProfileRequestNew(BaseModel):
    permission_level: str = Field(
        alias="permission-level",
        description="""The level of the Multi Domain Permissions Profile.<br>The level cannot be changed after creation.""",
    )
    mds_provisioning: bool = Field(
        alias="mds-provisioning",
        description="""Create and manage Multi-Domain Servers and Multi-Domain Log Servers.<br>Only a Super User permission-level profile can select this option.""",
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
        description="""Permission to log in to the Security Management Server and run API commands using these tools: mgmt_cli (Linux and Windows binaries), Gaia CLI (clish) and Web Services (REST). Useful if you want to prevent administrators from .running automatic scripts on the Management.<br>Note: This permission is not required to run commands from .within the API terminal in SmartConsole.""",
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
    default_profile_global_domains: str = Field(
        alias="default-profile-global-domains",
        description="""Name or UID of the required default profile for all global domains.""",
    )
    view_global_objects_in_domain: bool = Field(
        alias="view-global-objects-in-domain",
        description="""Lets an administrator with no global objects permissions view the global objects in the domain. This option is required for valid domain management.""",
    )
    enable_default_profile_for_local_domains: bool = Field(
        alias="enable-default-profile-for-local-domains",
        description="""Enable the option to specify a default profile for all local domains.""",
    )
    default_profile_local_domains: str = Field(
        alias="default-profile-local-domains",
        description="""Name or UID of the required default profile for all local domains.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
