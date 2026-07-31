from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class CustomTrustedCaCertificateReply(BaseModel):
    name: str = Field(alias="name", description="""Trusted CA certificate name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    added_by: str = Field(
        alias="added-by", description="""By whom the certificate was added."""
    )
    base64_certificate: str = Field(
        alias="base64-certificate", description="""The certificate in base64."""
    )
    issued_by: str = Field(
        alias="issued-by", description="""Trusted CA certificate issued by."""
    )
    issued_to: str = Field(
        alias="issued-to", description="""Trusted CA certificate issued to."""
    )
    valid_from: ApiDateReply = Field(
        alias="valid-from", description="""Trusted CA certificate valid from date."""
    )
    valid_to: ApiDateReply = Field(
        alias="valid-to", description="""Trusted CA certificate valid to date."""
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
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
