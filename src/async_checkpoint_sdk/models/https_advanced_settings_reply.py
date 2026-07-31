from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .bypass_under_load_reply import BypassUnderLoadReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field
from .server_cert_validation_actions_reply import ServerCertValidationActionsReply


class HttpsAdvancedSettingsReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    bypass_on_client_failure: bool = Field(
        alias="bypass-on-client-failure",
        description="""Whether all requests should be bypassed or blocked-in case of client errors (Client closes the connection due to authentication issues during handshake)<br><ul style=list-style-type:square><li>true - Fail-open (bypass all requests).</li><li>false - Fail-close (block all requests.</li></ul>.""",
    )
    bypass_on_failure: bool = Field(
        alias="bypass-on-failure",
        description="""Whether all requests should be bypassed or blocked-in case of server errors (for example validation error during GW-Server authentication)<br><ul style=list-style-type:square><li>true - Fail-open (bypass all requests).</li><li>false - Fail-close (block all requests.</li></ul>.""",
    )
    bypass_under_load: BypassUnderLoadReply = Field(
        alias="bypass-under-load",
        description="""Bypass the HTTPS Inspection temporarily to improve connectivity during a heavy load on the Security Gateway. The HTTPS Inspection would resume as soon as the load decreases.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    site_categorization_allow_mode: str = Field(
        alias="site-categorization-allow-mode",
        description="""Whether all requests should be allowed or blocked until categorization is complete.<br><ul style=list-style-type:square><li>Background - to allow requests until categorization is complete.</li><li>Hold- to block requests until categorization is complete.</li></ul>.""",
    )
    server_certificate_validation_actions: ServerCertValidationActionsReply = Field(
        alias="server-certificate-validation-actions",
        description="""When a Security Gateway receives an untrusted certificate from .a website server, define when to drop the connection and how to track it.""",
    )
    retrieve_intermediate_ca_certificates: bool = Field(
        alias="retrieve-intermediate-ca-certificates",
        description="""Configure the value true to use the Certificate Authority Information Access extension to retrieve certificates that are missing from .the certificate chain.""",
    )
    blocked_certificates: list[dict] = Field(
        alias="blocked-certificates",
        description="""Collection of certificates objects identified by serial number.<br>Drop traffic from .servers using the blocked certificate.""",
    )
    blocked_certificate_tracking: str = Field(
        alias="blocked-certificate-tracking",
        description="""Controls whether to log and send a notification for dropped traffic.<br><ul style=list-style-type:square><li>None - Does not record the event.</li><li>Log - Records the event details in SmartView.</li><li>Alert - Logs the event and executes a command.</li><li>Mail - Sends an email to the administrator.</li><li>SNMP Trap - Sends an SNMP alert to the SNMP GU.</li><li>User Defined Alert - Sends customized alerts.</li></ul>.""",
    )
    bypass_update_services: bool = Field(
        alias="bypass-update-services",
        description="""Configure the value true to bypass traffic to well-known software update services.""",
    )
    certificate_pinned_apps_action: str = Field(
        alias="certificate-pinned-apps-action",
        description="""Configure the value bypass to bypass traffic from .certificate-pinned applications approved by Check Point.<br>HTTPS Inspection cannot inspect connections initiated by certificate-pinned applications.<br>Configure the value detect to send logs for traffic from .certificate-pinned applications approved by Check Point.""",
    )
    log_sessions: bool = Field(
        alias="log-sessions",
        description="""The value true configures the Security Gateway to send HTTPS Inspection session logs.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
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
