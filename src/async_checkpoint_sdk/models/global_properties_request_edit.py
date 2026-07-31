from .add import add
from .authentication_global_properties_request import (
    AuthenticationGlobalPropertiesRequest,
)
from .carrier_security_global_properties_request import (
    CarrierSecurityGlobalPropertiesRequest,
)
from .connect_control_global_properties_request import (
    ConnectControlGlobalPropertiesRequest,
)
from .data_access_ctrl_global_properties_request import (
    DataAccessCtrlGlobalPropertiesRequest,
)
from .firewall_global_properties_request import FirewallGlobalPropertiesRequest
from .global_properties_advanced_conf_request import GlobalPropertiesAdvancedConfRequest
from .hit_count_global_properties_request import HitCountGlobalPropertiesRequest
from .identity_awareness_global_properties_request import (
    IdentityAwarenessGlobalPropertiesRequest,
)
from .ip_address_range_request import IpAddressRangeRequest
from .log_and_alert_global_properties_request import LogAndAlertGlobalPropertiesRequest
from .nat_global_properties_request import NatGlobalPropertiesRequest
from .proxy_global_properties_request import ProxyGlobalPropertiesRequest
from .pydantic import BaseModel, Field
from .qo_s_global_properties_request import QoSGlobalPropertiesRequest
from .remote_access_global_properties_request import RemoteAccessGlobalPropertiesRequest
from .remove import remove
from .stateful_inspection_global_properties_request import (
    StatefulInspectionGlobalPropertiesRequest,
)
from .user_accounts_global_properties_request import UserAccountsGlobalPropertiesRequest
from .user_authority_global_properties_request import (
    UserAuthorityGlobalPropertiesRequest,
)
from .user_check_global_properties_request import UserCheckGlobalPropertiesRequest
from .user_directory_global_properties_request import (
    UserDirectoryGlobalPropertiesRequest,
)
from .vpn_global_properties_request import VpnGlobalPropertiesRequest


class GlobalPropertiesRequestEdit(BaseModel):
    firewall: FirewallGlobalPropertiesRequest = Field(
        alias="firewall",
        description="""Add implied rules to or remove them from .the Firewall Rule Base. Determine the position of the implied rules in the Rule Base, and whether or not to log them.""",
    )
    nat: NatGlobalPropertiesRequest = Field(
        alias="nat",
        description="""Configure settings that apply to all NAT connections.""",
    )
    authentication: AuthenticationGlobalPropertiesRequest = Field(
        alias="authentication",
        description="""Define Authentication properties that are common to all users and to the various ways that the Check Point Security Gateway asks for passwords (User, Client and Session Authentication).""",
    )
    vpn: VpnGlobalPropertiesRequest = Field(
        alias="vpn", description="""Configure settings relevant to VPN."""
    )
    identity_awareness: IdentityAwarenessGlobalPropertiesRequest = Field(
        alias="identity-awareness",
        description="""Configure Identity Awareness properties.""",
    )
    remote_access: RemoteAccessGlobalPropertiesRequest = Field(
        alias="remote-access", description="""Configure Remote Access properties."""
    )
    user_directory: UserDirectoryGlobalPropertiesRequest = Field(
        alias="user-directory",
        description="""User can enable LDAP User Directory as well as specify global parameters for LDAP. If LDAP User Directory is enabled, this means that users are managed on an external LDAP server and not on the internal Check Point Security Gateway users databases.""",
    )
    qos: QoSGlobalPropertiesRequest = Field(
        alias="qos",
        description="""Define the general parameters of Quality of Service (QoS) and apply them to QoS rules.""",
    )
    carrier_security: CarrierSecurityGlobalPropertiesRequest = Field(
        alias="carrier-security",
        description="""Specify system-wide properties. Select GTP intra tunnel inspection options, including anti-spoofing; tracking and logging options, and integrity tests.""",
    )
    user_accounts: UserAccountsGlobalPropertiesRequest = Field(
        alias="user-accounts",
        description="""Set the expiration for a user account and configure about to expire warnings.""",
    )
    user_authority: UserAuthorityGlobalPropertiesRequest = Field(
        alias="user-authority",
        description="""Decide whether to display and access the WebAccess rule base. This policy defines which users (that is, which Windows Domains) have access to the internal sites of the organization.""",
    )
    connect_control: ConnectControlGlobalPropertiesRequest = Field(
        alias="connect-control",
        description="""Configure settings that relate to ConnectControl server load balancing.""",
    )
    stateful_inspection: StatefulInspectionGlobalPropertiesRequest = Field(
        alias="stateful-inspection",
        description="""Adjust Stateful Inspection parameters.""",
    )
    log_and_alert: LogAndAlertGlobalPropertiesRequest = Field(
        alias="log-and-alert",
        description="""Define system-wide logging and alerting parameters.""",
    )
    data_access_control: DataAccessCtrlGlobalPropertiesRequest = Field(
        alias="data-access-control",
        description="""Configure automatic downloads from .Check Point and anonymously share product data. Options selected here apply to all Security Gateways, Clusters and VSX devices managed by this management server.""",
    )
    non_unique_ip_address_ranges: add | remove | IpAddressRangeRequest | list[dict] = Field(
        alias="non-unique-ip-address-ranges",
        description="""Specify Non Unique IP Address Ranges.""",
    )
    proxy: ProxyGlobalPropertiesRequest = Field(
        alias="proxy",
        description="""Select whether a proxy server is used when servers, gateways, or clients need to access the internet for certain Check Point features and set the default proxy server that will be used.""",
    )
    user_check: UserCheckGlobalPropertiesRequest = Field(
        alias="user-check",
        description="""Set a language for the UserCheck message if the language setting in the user's browser cannot be determined.""",
    )
    hit_count: HitCountGlobalPropertiesRequest = Field(
        alias="hit-count",
        description="""Enable the Hit Count feature that tracks the number of connections that each rule matches.""",
    )
    advanced_conf: GlobalPropertiesAdvancedConfRequest = Field(
        alias="advanced-conf",
        description="""Configure advanced global attributes. It's highly recommended to consult with Check Point's Technical Support before modifying these values.""",
    )
    allow_remote_registration_of_opsec_products: bool = Field(
        alias="allow-remote-registration-of-opsec-products",
        description="""After installing an OPSEC application, the remote administration (RA) utility enables an OPSEC product to finish registering itself without having to access the SmartConsole. If set to true, any host including the application host can run the utility. Otherwise,  the RA utility can only be run from .the Security Management host.""",
    )
    num_spoofing_errs_that_trigger_brute_force: int = Field(
        alias="num-spoofing-errs-that-trigger-brute-force",
        description="""Indicates how many incorrectly signed packets will be tolerated before assuming that there is an attack on the packet tagging and revoking the client's key.""",
    )
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
