from .api_domain_identifier import ApiDomainIdentifier
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class LoginRestrictionsReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    lockout_admin_account: bool = Field(
        alias="lockout-admin-account",
        description="""Indicates whether to lockout administrator's account after specified number of failed authentication attempts.""",
    )
    failed_authentication_attempts: int = Field(
        alias="failed-authentication-attempts",
        description="""Number of failed authentication attempts before lockout administrator account. <font color=red>Required only when</font> lockout-admin-account is set to true.""",
    )
    unlock_admin_account: bool = Field(
        alias="unlock-admin-account",
        description="""Indicates whether to unlock administrator account after specified number of minutes. <font color=red>Required only when</font> lockout-admin-account is set to true.""",
    )
    lockout_duration: int = Field(
        alias="lockout-duration",
        description="""Number of minutes of administrator account lockout. <font color=red>Required only when</font> lockout-admin-account is set to true.""",
    )
    display_access_denied_message: bool = Field(
        alias="display-access-denied-message",
        description="""Indicates whether to display informative message upon denying access. <font color=red>Required only when</font> lockout-admin-account is set to true.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
