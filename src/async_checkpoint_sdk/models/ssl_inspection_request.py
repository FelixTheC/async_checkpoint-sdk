from bypass_on_client_failure_request import BypassOnClientFailureRequest
from bypass_on_failure_request import BypassOnFailureRequest
from bypass_under_load_per_g_w_request import BypassUnderLoadPerGWRequest
from deny_expired_server_cert_request import DenyExpiredServerCertRequest
from deny_revoked_server_cert_request import DenyRevokedServerCertRequest
from deny_untrusted_server_cert_request import DenyUntrustedServerCertRequest
from outbound_certificate_override_request import OutboundCertificateOverrideRequest
from pydantic import BaseModel, Field
from site_categorization_allow_mode_request import SiteCategorizationAllowModeRequest


class SslInspectionRequest(BaseModel):
    bypass_on_client_failure: BypassOnClientFailureRequest = Field(
        alias="bypass-on-client-failure",
        description="""Controls whether to bypass all HTTPS requests (Fail-open mode) if there are errors on a client (for example, the client closes the connection due to authentication issues during a handshake).""",
    )
    bypass_on_failure: BypassOnFailureRequest = Field(
        alias="bypass-on-failure",
        description="""Set to be true in order to bypass all requests (Fail-open) in case of internal system error.""",
    )
    bypass_under_load: BypassUnderLoadPerGWRequest = Field(
        alias="bypass-under-load",
        description="""Bypass the HTTPS Inspection temporarily to improve connectivity during a heavy load on the Security Gateway. The HTTPS Inspection would resume as soon as the load decreases.""",
    )
    site_categorization_allow_mode: SiteCategorizationAllowModeRequest = Field(
        alias="site-categorization-allow-mode",
        description="""Set to 'background' in order to allowed requests until categorization is complete.""",
    )
    deny_untrusted_server_cert: DenyUntrustedServerCertRequest = Field(
        alias="deny-untrusted-server-cert",
        description="""Set to be true in order to drop traffic from servers with untrusted server certificate. The global value can be set in HTTPS Advanced Settings under server certificate validation object.""",
    )
    deny_revoked_server_cert: DenyRevokedServerCertRequest = Field(
        alias="deny-revoked-server-cert",
        description="""Set to be true in order to drop traffic from servers with revoked server certificate (validate CRL). The global value can be set in HTTPS Advanced Settings under server certificate validation object.""",
    )
    deny_expired_server_cert: DenyExpiredServerCertRequest = Field(
        alias="deny-expired-server-cert",
        description="""Set to be true in order to drop traffic from servers with expired server certificate. The global value can be set in HTTPS Advanced Settings under server certificate validation object.""",
    )
    outbound_certificate: OutboundCertificateOverrideRequest = Field(
        alias="outbound-certificate",
        description="""Set to be true in order to use a specific Outbound Certificate.""",
    )
    deployment_mode: str = Field(
        alias="deployment-mode",
        description="""* Full inspection - According to the configured HTTPS Inspection policy.<br>* Learning mode - Inspect a small percentage of the traffic to identify issues and estimate the expected resource consumption of the configured HTTPS Inspection policy.""",
    )
