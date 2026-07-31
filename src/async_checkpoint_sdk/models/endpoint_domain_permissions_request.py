from .pydantic import BaseModel, Field


class EndpointDomainPermissionsRequest(BaseModel):
    manage_policies_and_software_deployment: bool = Field(
        alias="manage-policies-and-software-deployment",
        description="""The administrator can work with policies, rules and actions.""",
    )
    edit_endpoint_policies: bool = Field(
        alias="edit-endpoint-policies",
        description="""Available only if manage-policies-and-software-deployment is set to true.""",
    )
    policies_installation: bool = Field(
        alias="policies-installation",
        description="""The administrator can install policies on endpoint computers.""",
    )
    edit_software_deployment: bool = Field(
        alias="edit-software-deployment",
        description="""The administrator can define deployment rules, create packages for export, and configure advanced package settings.<br>Available only if manage-policies-and-software-deployment is set to true.""",
    )
    software_deployment_installation: bool = Field(
        alias="software-deployment-installation",
        description="""The administrator can deploy packages and install endpoint clients.""",
    )
    allow_executing_push_operations: bool = Field(
        alias="allow-executing-push-operations",
        description="""The administrator can start operations that the Security Management Server pushes directly to client computers with no policy installation required.""",
    )
    authorize_preboot_users: bool = Field(
        alias="authorize-preboot-users",
        description="""The administrator can add and remove the users who are permitted to log on to Endpoint Security client computers with Full Disk Encryption.""",
    )
    recovery_media: bool = Field(
        alias="recovery-media",
        description="""The administrator can create recovery media on endpoint computers and devices.""",
    )
    remote_help: bool = Field(
        alias="remote-help",
        description="""The administrator can use the Remote Help feature to reset user passwords and give access to locked out users.""",
    )
    reset_computer_data: bool = Field(
        alias="reset-computer-data",
        description="""The administrator can reset a computer, which deletes all information about the computer from .the Security Management Server.""",
    )
