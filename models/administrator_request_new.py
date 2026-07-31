from folder_permissions_role_pair_request import FolderPermissionsRolePairRequest
from pydantic import BaseModel, Field


class AdministratorRequestNew(BaseModel):
    authentication_method: str = Field(
        alias="authentication-method", description="""Authentication method."""
    )
    email: str = Field(alias="email", description="""Administrator email.""")
    expiration_date: str = Field(
        alias="expiration-date",
        description="""Format: YYYY-MM-DD. <br>If you configure an expiration for an administrator user, then the user is not logged out automatically. Only a new login is blocked.""",
    )
    multi_domain_profile: str = Field(
        alias="multi-domain-profile",
        description="""Administrator multi-domain profile.""",
    )
    must_change_password: bool = Field(
        alias="must-change-password",
        description="""True if administrator must change password on the next login.""",
    )
    password: str = Field(alias="password", description="""Administrator password.""")
    password_hash: str = Field(
        alias="password-hash", description="""Administrator password hash."""
    )
    permissions_profile: FolderPermissionsRolePairRequest | list[dict] = Field(
        alias="permissions-profile",
        description="""Administrator permissions profile. Permissions profile should not be provided when multi-domain-profile is set to Multi-Domain Super User or Domain Super User.""",
    )
    phone_number: str = Field(
        alias="phone-number", description="""Administrator phone number."""
    )
    radius_server: str = Field(
        alias="radius-server",
        description="""RADIUS server object identified by the name or UID. Must be set when authentication-method was selected to be RADIUS.""",
    )
    tacacs_server: str = Field(
        alias="tacacs-server",
        description="""TACACS server object identified by the name or UID. Must be set when authentication-method was selected to be TACACS.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
