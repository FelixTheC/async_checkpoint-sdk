from pydantic import BaseModel, Field
from site_categorization_allow_mode_reply import SiteCategorizationAllowModeReply
from ssl_inspection_override_boolean_reply import SslInspectionOverrideBooleanReply


class SslInspectionReply(BaseModel):
    bypass_on_failure: SslInspectionOverrideBooleanReply = Field(
        alias="bypass-on-failure",
        description="""Set to be true in order to bypass all requests (Fail-open) in case of internal system error.""",
    )
    site_categorization_allow_mode: SiteCategorizationAllowModeReply = Field(
        alias="site-categorization-allow-mode",
        description="""Set to 'background' in order to allowed requests until categorization is complete.""",
    )
    deny_untrusted_server_cert: SslInspectionOverrideBooleanReply = Field(
        alias="deny-untrusted-server-cert",
        description="""Set to be true in order to drop traffic from servers with untrusted server certificate.""",
    )
    deny_revoked_server_cert: SslInspectionOverrideBooleanReply = Field(
        alias="deny-revoked-server-cert",
        description="""Set to be true in order to drop traffic from servers with revoked server certificate (validate CRL).""",
    )
    deny_expired_server_cert: SslInspectionOverrideBooleanReply = Field(
        alias="deny-expired-server-cert",
        description="""Set to be true in order to drop traffic from servers with expired server certificate.""",
    )
