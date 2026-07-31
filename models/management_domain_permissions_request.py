from pydantic import BaseModel, Field


class ManagementDomainPermissionsRequest(BaseModel):
    cme_operations: str = Field(
        alias="cme-operations",
        description="""Permission to read / edit the Cloud Management Extension (CME) configuration.<br>Not supported for Multi-Domain Servers.""",
    )
    manage_admins: bool = Field(
        alias="manage-admins",
        description="""Controls the ability to manage Administrators, Permission Profiles, Trusted clients,API settings and Policy settings.<br>Only a Read Write All permission-type profile can edit this permission.<br>Not supported for Multi-Domain Servers.""",
    )
    management_api_login: bool = Field(
        alias="management-api-login",
        description="""Permission to log in to the Security Management Server and run API commands using these tools: mgmt_cli (Linux and Windows binaries), Gaia CLI (clish) and Web Services (REST). Useful if you want to prevent administrators from running automatic scripts on the Management.<br>Note: This permission is not required to run commands from within the API terminal in SmartConsole.<br>Not supported for Multi-Domain Servers.""",
    )
    manage_sessions: bool = Field(
        alias="manage-sessions",
        description="""Lets you disconnect, discard, publish, or take over other administrator sessions.<br>Only a Read Write All permission-type profile can edit this permission.""",
    )
    high_availability_operations: bool = Field(
        alias="high-availability-operations",
        description="""Configure and work with Domain High Availability.<br>Only a 'Customized' permission-type profile can edit this permission.""",
    )
    approve_or_reject_sessions: bool = Field(
        alias="approve-or-reject-sessions",
        description="""Approve / reject other sessions.""",
    )
    publish_sessions: bool = Field(
        alias="publish-sessions",
        description="""Allow session publishing without an approval.""",
    )
    manage_integration_with_cloud_services: bool = Field(
        alias="manage-integration-with-cloud-services",
        description="""Manage integration with Cloud Services.""",
    )
