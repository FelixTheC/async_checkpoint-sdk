from add import Add
from pydantic import BaseModel, Field
from remove import Remove
from user_encryption_request import UserEncryptionRequest
from user_locations_request_edit import UserLocationsRequestEdit


class UserRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    email: str = Field(alias="email", description="""User email.""")
    expiration_date: str = Field(
        alias="expiration-date", description="""Expiration date in format: yyyy-MM-dd."""
    )
    phone_number: str = Field(alias="phone-number", description="""User phone number.""")
    authentication_method: str = Field(
        alias="authentication-method", description="""Authentication method."""
    )
    password: str = Field(
        alias="password",
        description="""Check Point password authentication method identified by the name or UID. Must be set when authentication-method was selected to be Check Point Password.""",
    )
    radius_server: str = Field(
        alias="radius-server",
        description="""RADIUS server object identified by the name or UID. Must be set when authentication-method was selected to be RADIUS.""",
    )
    tacacs_server: str = Field(
        alias="tacacs-server",
        description="""TACACS server object identified by the name or UID. Must be set when authentication-method was selected to be TACACS.""",
    )
    connect_on_days: list[str] = Field(
        alias="connect-on-days", description="""Days users allow to connect."""
    )
    from_hour: str = Field(alias="from-hour", description="""Allow users connect from hour.""")
    to_hour: str = Field(alias="to-hour", description="""Allow users connect until hour.""")
    allowed_locations: UserLocationsRequestEdit = Field(
        alias="allowed-locations", description="""User allowed locations."""
    )
    certificates: Add | Remove = Field(alias="certificates", description="""User certificates.""")
    encryption: UserEncryptionRequest = Field(
        alias="encryption", description="""User encryption."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    groups: Add | Remove | str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
