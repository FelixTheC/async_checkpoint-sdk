from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class IdentityProviderReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    usage: str = Field(alias="usage", description="""Usage of Identity Provider.""")
    gateway: ApiObjectStandardIdentifier = Field(
        alias="gateway",
        description="""Gateway for the SAML Identity Provider usage. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    service: str = Field(alias="service", description="""Service for the selected gateway.""")
    required_identifier: str = Field(
        alias="required-identifier",
        description="""Required identifier (Entity ID) for the SAML Identity Provider.""",
    )
    reply_urls: list[str] = Field(
        alias="reply-urls",
        description="""List of URLs for the SAML Identity Provider.""",
    )
    data_receiving: str = Field(
        alias="data-receiving",
        description="""Data receiving method from .the SAML Identity Provider.""",
    )
    received_identifier: str = Field(
        alias="received-identifier",
        description="""Identifier (Entity ID) based on the provider data.""",
    )
    login_url: str = Field(
        alias="login-url", description="""Login URL based on the provider data."""
    )
    base64_metadata_file: str = Field(
        alias="base64-metadata-file",
        description="""Metadata file encoded in base64 based on the provider data.""",
    )
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64 based on provider data.""",
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
