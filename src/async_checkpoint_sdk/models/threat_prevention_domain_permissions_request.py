from .pydantic import BaseModel, Field


class ThreatPreventionDomainPermissionsRequest(BaseModel):
    policy_layers: str = Field(
        alias="policy-layers",
        description="""Configure Threat Prevention Policy rules.<br>Note: To have policy-layers permissions you must set policy-exceptions and profiles permissions. To have 'Write' permissions for policy-layers, policy-exceptions must be set with 'Write' permission as well.""",
    )
    edit_layers: str = Field(
        alias="edit-layers",
        description="""'ALL' -  Gives permission to edit all layers.<br>By Selected Profile In A Layer Editor -  Administrators can only edit the layer if the Threat Prevention layer editor gives editing permission to their profiles.<br>Available only if policy-layers is set to 'Write'.""",
    )
    edit_settings: bool = Field(
        alias="edit-settings",
        description="""Work with general Threat Prevention settings.""",
    )
    policy_exceptions: str = Field(
        alias="policy-exceptions",
        description="""Configure exceptions to Threat Prevention rules.<br>Note: To have policy-exceptions you must set the protections permission.""",
    )
    profiles: str = Field(alias="profiles", description="""Configure Threat Prevention profiles.""")
    protections: str = Field(alias="protections", description="""Work with malware protections.""")
    install_policy: bool = Field(alias="install-policy", description="""Install Policies.""")
    ips_update: bool = Field(
        alias="ips-update",
        description="""Update IPS protections.<br>Note: You do not have to log into the User Center to receive IPS updates.""",
    )
