from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class OutboundCertificateReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64.""",
    )
    base64_public_certificate: str = Field(
        alias="base64-public-certificate",
        description="""Public Certificate file encoded in base64 (pem format).""",
    )
    issued_by: str = Field(
        alias="issued-by",
        description="""The DN (Distinguished Name) of the certificate.""",
    )
    public_key_algorithm: str = Field(
        alias="public-key-algorithm",
        description="""Public key algorithm and size of the outbound certificate.""",
    )
    subject: str = Field(alias="subject", description="""Certificate's subject.""")
    valid_from: str = Field(
        alias="valid-from", description="""Outbound certificate valid from .date."""
    )
    valid_to: str = Field(
        alias="valid-to", description="""Outbound certificate valid up to date."""
    )
    is_default: bool = Field(
        alias="is-default",
        description="""Is the certificate the default certificate.""",
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
