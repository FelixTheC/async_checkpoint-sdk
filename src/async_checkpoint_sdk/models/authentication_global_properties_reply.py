from .pydantic import BaseModel, Field


class AuthenticationGlobalPropertiesReply(BaseModel):
    auth_internal_users_with_specific_suffix: bool = Field(
        alias="auth-internal-users-with-specific-suffix",
        description="""Enforce suffix for internal users authentication.""",
    )
    allowed_suffix_for_internal_users: str = Field(
        alias="allowed-suffix-for-internal-users",
        description="""Suffix for internal users authentication.""",
    )
    max_days_before_expiration_of_non_pulled_user_certificates: int = Field(
        alias="max-days-before-expiration-of-non-pulled-user-certificates",
        description="""Users certificates which were initiated but not pulled will expire after the specified number of days. Any value from .1 to 60 days can be entered in this field.""",
    )
    max_client_auth_attempts_before_connection_termination: int = Field(
        alias="max-client-auth-attempts-before-connection-termination",
        description="""Allowed Number of Failed Client Authentication Attempts Before Session Termination. Any value from .1 to 800 attempts can be entered in this field.""",
    )
    max_rlogin_attempts_before_connection_termination: int = Field(
        alias="max-rlogin-attempts-before-connection-termination",
        description="""Allowed Number of Failed rlogin Attempts Before Session Termination. Any value from .1 to 800 attempts can be entered in this field.""",
    )
    max_session_auth_attempts_before_connection_termination: int = Field(
        alias="max-session-auth-attempts-before-connection-termination",
        description="""Allowed Number of Failed Session Authentication Attempts Before Session Termination. Any value from .1 to 800 attempts can be entered in this field.""",
    )
    max_telnet_attempts_before_connection_termination: int = Field(
        alias="max-telnet-attempts-before-connection-termination",
        description="""Allowed Number of Failed telnet Attempts Before Session Termination. Any value from .1 to 800 attempts can be entered in this field.""",
    )
    enable_delayed_auth: bool = Field(
        alias="enable-delayed-auth",
        description="""all authentications other than certificate-based authentications will be delayed by the specified time. Applying this delay will stall brute force authentication attacks. The delay is applied for both failed and successful authentication attempts.""",
    )
    delay_each_auth_attempt_by: int = Field(
        alias="delay-each-auth-attempt-by",
        description="""Delay each authentication attempt by the specified number of milliseconds. Any value from .1 to 25000 can be entered in this field.""",
    )
