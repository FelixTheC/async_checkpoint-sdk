from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class AdministratorReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    authentication_method: str = Field(
        alias="authentication-method", description="""Authentication method."""
    )
    email: str = Field(alias="email", description="""Administrator email.""")
    expiration_date: ApiDateReply = Field(alias="expiration-date", description="""N/A""")
    multi_domain_profile: list[dict] = Field(
        alias="multi-domain-profile",
        description="""Administrator multi-domain profile. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    must_change_password: bool = Field(
        alias="must-change-password",
        description="""True if administrator must change password on the next login.""",
    )
    permissions_profile: list[dict] = Field(
        alias="permissions-profile",
        description="""Administrator permissions profile. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    phone_number: str = Field(alias="phone-number", description="""Administrator phone number.""")
    radius_server: ApiObjectStandardIdentifier = Field(
        alias="radius-server",
        description="""RADIUS server object identified by the name or UID. Must be set when authentication-method was selected to be RADIUS. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    sic_name: str = Field(
        alias="sic-name", description="""Name of the Secure Internal Connection Trust."""
    )
    tacacs_server: ApiObjectStandardIdentifier = Field(
        alias="tacacs-server",
        description="""TACACS server object identified by the name or UID . Must be set when authentication-method was selected to be TACACS. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
