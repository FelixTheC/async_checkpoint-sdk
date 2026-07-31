from api_domain_identifier import ApiDomainIdentifier
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class CpPasswordRequirementsReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    min_password_length: int = Field(
        alias="min-password-length", description="""Minimum Check Point password length."""
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
