from pydantic import BaseModel, Field


class UserDirectoryGlobalPropertiesReply(BaseModel):
    enable_password_change_when_user_active_directory_expires: bool = Field(
        alias="enable-password-change-when-user-active-directory-expires",
        description="""For organizations using MS Active Directory, this setting enables users whose passwords have expired to automatically create new passwords.""",
    )
    cache_size: int = Field(
        alias="cache-size",
        description="""The maximum number of cached users allowed. The cache is FIFO (first-in, first-out). When a new user is added to a full cache, the first user is deleted to make room for the new user. The Check Point Security Gateway does not query the LDAP server for users already in the cache, unless the cache has timed out.""",
    )
    enable_password_expiration_configuration: bool = Field(
        alias="enable-password-expiration-configuration",
        description="""Enable configuring of the number of days during which the password is valid.<br>If enable-password-change-when-user-active-directory-expires is true, the password expiration time is determined by the Active Directory. In this case it is recommended not to set this to true.""",
    )
    password_expires_after: int = Field(
        alias="password-expires-after",
        description="""Specifies the number of days during which the password is valid. Users are authenticated using a special LDAP password. Should this password expire, a new password must be defined.<br>Available only if enable-password-expiration-configuration is true.""",
    )
    timeout_on_cached_users: int = Field(
        alias="timeout-on-cached-users",
        description="""The period of time in which a cached user is timed out and will need to be fetched again from the LDAP server.""",
    )
    display_user_dn_at_login: str = Field(
        alias="display-user-dn-at-login",
        description="""Decide whether or not you would like to display the user's DN when logging in. If you choose to display the user DN, you can select whether to display it, when the user is prompted for the password at login, or on the request of the authentication scheme. This property is a useful diagnostic tool when there is more than one user with the same name in an Account Unit. In this case, the first one is chosen and the others are ignored.""",
    )
    enforce_rules_for_user_mgmt_admins: bool = Field(
        alias="enforce-rules-for-user-mgmt-admins",
        description="""Enforces password strength rules on LDAP users when you create or modify a Check Point Password.""",
    )
    min_password_length: int = Field(
        alias="min-password-length",
        description="""Specifies the minimum length (in characters) of the password.""",
    )
    password_must_include_a_digit: bool = Field(
        alias="password-must-include-a-digit", description="""Password must include a digit."""
    )
    password_must_include_a_symbol: bool = Field(
        alias="password-must-include-a-symbol", description="""Password must include a symbol."""
    )
    password_must_include_lowercase_char: bool = Field(
        alias="password-must-include-lowercase-char",
        description="""Password must include a lowercase character.""",
    )
    password_must_include_uppercase_char: bool = Field(
        alias="password-must-include-uppercase-char",
        description="""Password must include an uppercase character.""",
    )
