from add import add
from blocked_cert_request import BlockedCertRequest
from bypass_under_load_request import BypassUnderLoadRequest
from pydantic import BaseModel, Field
from remove import remove
from server_cert_validation_actions_request import ServerCertValidationActionsRequest
from update import update


class HttpsAdvancedSettingsRequest(BaseModel):
    bypass_on_client_failure: bool = Field(
        alias="bypass-on-client-failure",
        description="""Whether all requests should be bypassed or blocked-in case of client errors (Client closes the connection due to authentication issues during handshake)<br><ul style=list-style-type:square><li>true - Fail-open (bypass all requests).</li><li>false - Fail-close (block all requests.</li></ul><br>The default value is true.""",
    )
    bypass_on_failure: bool = Field(
        alias="bypass-on-failure",
        description="""Whether all requests should be bypassed or blocked-in case of server errors (for example validation error during GW-Server authentication)<br><ul style=list-style-type:square><li>true - Fail-open (bypass all requests).</li><li>false - Fail-close (block all requests.</li></ul><br>The default value is true.""",
    )
    bypass_under_load: BypassUnderLoadRequest = Field(
        alias="bypass-under-load",
        description="""Bypass the HTTPS Inspection temporarily to improve connectivity during a heavy load on the Security Gateway. The HTTPS Inspection would resume as soon as the load decreases.""",
    )
    site_categorization_allow_mode: str = Field(
        alias="site-categorization-allow-mode",
        description="""Whether all requests should be allowed or blocked until categorization is complete.<br><ul style=list-style-type:square><li>Background - to allow requests until categorization is complete.</li><li>Hold- to block requests until categorization is complete.</li></ul><br>The default value is hold.""",
    )
    server_certificate_validation_actions: ServerCertValidationActionsRequest = Field(
        alias="server-certificate-validation-actions",
        description="""When a Security Gateway receives an untrusted certificate from a website server, define when to drop the connection and how to track it.""",
    )
    retrieve_intermediate_ca_certificates: bool = Field(
        alias="retrieve-intermediate-ca-certificates",
        description="""Configure the value true to use the Certificate Authority Information Access extension to retrieve certificates that are missing from the certificate chain.<br>The default value is true.""",
    )
    blocked_certificates: add | remove | update | BlockedCertRequest | list[dict] = (
        Field(
            alias="blocked-certificates",
            description="""Collection of certificates objects identified by serial number.<br>Drop traffic from servers using the blocked certificate.""",
        )
    )
    blocked_certificate_tracking: str = Field(
        alias="blocked-certificate-tracking",
        description="""Controls whether to log and send a notification for dropped traffic.<br><ul style=list-style-type:square><li>None - Does not record the event.</li><li>Log - Records the event details in SmartView.</li><li>Alert - Logs the event and executes a command.</li><li>Mail - Sends an email to the administrator.</li><li>SNMP Trap - Sends an SNMP alert to the SNMP GU.</li><li>User Defined Alert - Sends customized alerts.</li></ul>.""",
    )
    bypass_update_services: bool = Field(
        alias="bypass-update-services",
        description="""Configure the value true to bypass traffic to well-known software update services.<br>The default value is true.""",
    )
    certificate_pinned_apps_action: str = Field(
        alias="certificate-pinned-apps-action",
        description="""Configure the value bypass to bypass traffic from certificate-pinned applications approved by Check Point.<br>HTTPS Inspection cannot inspect connections initiated by certificate-pinned applications.<br>Configure the value detect to send logs for traffic from certificate-pinned applications approved by Check Point.<br>The default value is bypass.""",
    )
    log_sessions: bool = Field(
        alias="log-sessions",
        description="""The value true configures the Security Gateway to send HTTPS Inspection session logs.<br>The default value is true.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
