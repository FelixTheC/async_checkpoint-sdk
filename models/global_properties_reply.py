from api_domain_identifier import ApiDomainIdentifier
from authentication_global_properties_reply import AuthenticationGlobalPropertiesReply
from available_actions_reply import AvailableActionsReply
from carrier_security_global_properties_reply import (
    CarrierSecurityGlobalPropertiesReply,
)
from connect_control_global_properties_reply import ConnectControlGlobalPropertiesReply
from data_access_ctrl_global_properties_reply import DataAccessCtrlGlobalPropertiesReply
from firewall_global_properties_reply import FirewallGlobalPropertiesReply
from global_properties_advanced_conf_reply import GlobalPropertiesAdvancedConfReply
from hit_count_global_properties_reply import HitCountGlobalPropertiesReply
from identity_awareness_global_properties_reply import (
    IdentityAwarenessGlobalPropertiesReply,
)
from log_and_alert_global_properties_reply import LogAndAlertGlobalPropertiesReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from nat_global_properties_reply import NatGlobalPropertiesReply
from proxy_global_properties_reply import ProxyGlobalPropertiesReply
from pydantic import BaseModel, Field
from qo_s_global_properties_reply import QoSGlobalPropertiesReply
from remote_access_global_properties_reply import RemoteAccessGlobalPropertiesReply
from stateful_inspection_global_properties_reply import (
    StatefulInspectionGlobalPropertiesReply,
)
from user_accounts_global_properties_reply import UserAccountsGlobalPropertiesReply
from user_authority_global_properties_reply import UserAuthorityGlobalPropertiesReply
from user_check_global_properties_reply import UserCheckGlobalPropertiesReply
from user_directory_global_properties_reply import UserDirectoryGlobalPropertiesReply
from vpn_global_properties_reply import VpnGlobalPropertiesReply


class GlobalPropertiesReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    firewall: FirewallGlobalPropertiesReply = Field(
        alias="firewall",
        description="""Add implied rules to or remove them from the Firewall Rule Base. Determine the position of the implied rules in the Rule Base, and whether or not to log them.""",
    )
    identity_awareness: IdentityAwarenessGlobalPropertiesReply = Field(
        alias="identity-awareness",
        description="""Configure Identity Awareness properties.""",
    )
    nat: NatGlobalPropertiesReply = Field(
        alias="nat",
        description="""Configure settings that apply to all NAT connections.""",
    )
    authentication: AuthenticationGlobalPropertiesReply = Field(
        alias="authentication",
        description="""Define Authentication properties that are common to all users and to the various ways that the Check Point Security Gateway asks for passwords (User, Client and Session Authentication).""",
    )
    vpn: VpnGlobalPropertiesReply = Field(
        alias="vpn", description="""Configure settings relevant to VPN."""
    )
    remote_access: RemoteAccessGlobalPropertiesReply = Field(
        alias="remote-access", description="""Configure Remote Access properties."""
    )
    user_directory: UserDirectoryGlobalPropertiesReply = Field(
        alias="user-directory",
        description="""User can enable LDAP User Directory as well as specify global parameters for LDAP. If LDAP User Directory is enabled, this means that users are managed on an external LDAP server and not on the internal Check Point Security Gateway users databases.""",
    )
    qos: QoSGlobalPropertiesReply = Field(
        alias="qos",
        description="""Define the general parameters of Quality of Service (QoS) and apply them to QoS rules.""",
    )
    carrier_security: CarrierSecurityGlobalPropertiesReply = Field(
        alias="carrier-security",
        description="""Specify system-wide properties. Select GTP intra tunnel inspection options, including anti-spoofing; tracking and logging options, and integrity tests.""",
    )
    user_accounts: UserAccountsGlobalPropertiesReply = Field(
        alias="user-accounts",
        description="""Set the expiration for a user account and configure about to expire warnings.""",
    )
    user_authority: UserAuthorityGlobalPropertiesReply = Field(
        alias="user-authority",
        description="""Decide whether to display and access the WebAccess rule base. This policy defines which users (that is, which Windows Domains) have access to the internal sites of the organization.""",
    )
    connect_control: ConnectControlGlobalPropertiesReply = Field(
        alias="connect-control",
        description="""Configure settings that relate to ConnectControl server load balancing.""",
    )
    stateful_inspection: StatefulInspectionGlobalPropertiesReply = Field(
        alias="stateful-inspection",
        description="""Adjust Stateful Inspection parameters.""",
    )
    log_and_alert: LogAndAlertGlobalPropertiesReply = Field(
        alias="log-and-alert",
        description="""Define system-wide logging and alerting parameters.""",
    )
    data_access_control: DataAccessCtrlGlobalPropertiesReply = Field(
        alias="data-access-control",
        description="""Configure automatic downloads from Check Point and anonymously share product data. Options selected here apply to all Security Gateways, Clusters and VSX devices managed by this management server.""",
    )
    non_unique_ip_address_ranges: list[dict] = Field(
        alias="non-unique-ip-address-ranges",
        description="""Specify Non Unique IP Address Ranges.""",
    )
    proxy: ProxyGlobalPropertiesReply = Field(
        alias="proxy",
        description="""Select whether a proxy server is used when servers, gateways, or clients need to access the internet for certain Check Point features and set the default proxy server that will be used.""",
    )
    user_check: UserCheckGlobalPropertiesReply = Field(
        alias="user-check",
        description="""Set a language for the UserCheck message if the language setting in the user's browser cannot be determined.""",
    )
    hit_count: HitCountGlobalPropertiesReply = Field(
        alias="hit-count",
        description="""Enable the Hit Count feature that tracks the number of connections that each rule matches.""",
    )
    advanced_conf: GlobalPropertiesAdvancedConfReply = Field(
        alias="advanced-conf",
        description="""Configure advanced global attributes. It's highly recommended to consult with Check Point's Technical Support before modifying these values.""",
    )
    allow_remote_registration_of_opsec_products: bool = Field(
        alias="allow-remote-registration-of-opsec-products",
        description="""After installing an OPSEC application, the remote administration (RA) utility enables an OPSEC product to finish registering itself without having to access the SmartConsole. If set to true, any host including the application host can run the utility. Otherwise,  the RA utility can only be run from the Security Management host.""",
    )
    num_spoofing_errs_that_trigger_brute_force: int = Field(
        alias="num-spoofing-errs-that-trigger-brute-force",
        description="""Indicates how many incorrectly signed packets will be tolerated before assuming that there is an attack on the packet tagging and revoking the client's key.""",
    )
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
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
