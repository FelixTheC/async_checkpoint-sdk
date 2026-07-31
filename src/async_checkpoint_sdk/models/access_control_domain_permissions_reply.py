from access_control_policy_layers_domain_permissions_reply import (
    AccessControlPolicyLayersDomainPermissionsReply,
)
from pydantic import BaseModel, Field


class AccessControlDomainPermissionsReply(BaseModel):
    show_policy: bool = Field(
        alias="show-policy",
        description="""Select to let administrators work with Access Control rules and NAT rules. If not selected, administrators cannot see these rules.""",
    )
    policy_layers: AccessControlPolicyLayersDomainPermissionsReply = Field(
        alias="policy-layers",
        description="""Layer editing permissions.<br>Available only if show-policy is set to true.""",
    )
    dlp_policy: str = Field(alias="dlp-policy", description="""Configure DLP rules and Policies.""")
    geo_control_policy: str = Field(
        alias="geo-control-policy",
        description="""Work with Access Control rules that control traffic to and from specified countries.""",
    )
    nat_policy: str = Field(
        alias="nat-policy", description="""Work with NAT in Access Control rules."""
    )
    qos_policy: str = Field(alias="qos-policy", description="""Work with QoS Policies and rules.""")
    access_control_objects_and_settings: str = Field(
        alias="access-control-objects-and-settings",
        description="""Allow editing of the following objet types: VPN Community, Access Role, Custom application group, Custom application, Custom category, Limit, Application - Match Settings, Application Category - Match Settings, Override Categorization, Application and URL filtering blade - Advanced Settings, Content Awareness blade - Advanced Settings.""",
    )
    app_control_and_url_filtering_update: bool = Field(
        alias="app-control-and-url-filtering-update",
        description="""Install Application and URL Filtering updates.""",
    )
    install_policy: bool = Field(
        alias="install-policy", description="""Install Access Control Policies."""
    )
