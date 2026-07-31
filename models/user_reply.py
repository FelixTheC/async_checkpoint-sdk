from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from user_encryption_reply import UserEncryptionReply
from user_locations_reply import UserLocationsReply


class UserReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    email: str = Field(alias="email", description="""User email.""")
    expiration_date: ApiDateReply = Field(
        alias="expiration-date", description="""User expiration date."""
    )
    phone_number: str = Field(
        alias="phone-number", description="""User phone number."""
    )
    type: str = Field(alias="type", description="""Object type.""")
    authentication_method: str = Field(
        alias="authentication-method", description="""Authentication method."""
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    radius_server: ApiObjectStandardIdentifier = Field(
        alias="radius-server",
        description="""RADIUS server object identified by the name or UID. Must be set when authentication-method was selected to be RADIUS. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    tacacs_server: ApiObjectStandardIdentifier = Field(
        alias="tacacs-server",
        description="""TACACS server object identified by the name or UID. Must be set when authentication-method was selected to be TACACS. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    connect_daily: bool = Field(
        alias="connect-daily", description="""Connect every day."""
    )
    connect_on_days: list[str] = Field(
        alias="connect-on-days", description="""Days users allow to connect."""
    )
    from_hour: str = Field(alias="from-hour", description="""Connect from hour.""")
    to_hour: str = Field(alias="to-hour", description="""Connect to hour.""")
    allowed_locations: UserLocationsReply = Field(
        alias="allowed-locations", description="""User allowed locations."""
    )
    certificates: list[dict] = Field(
        alias="certificates", description="""User certificates."""
    )
    encryption: UserEncryptionReply = Field(
        alias="encryption", description="""User encryption."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
