from .api_domain_identifier import ApiDomainIdentifier
from .pydantic import BaseModel, Field


class GatewayGlobalUseReply(BaseModel):
    name: str = Field(alias="name", description="""Target name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    enable_vpn: bool = Field(
        alias="enable-vpn",
        description="""Indicates whether VPN global use is enabled on the target.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    enable_identity_sharing: bool = Field(
        alias="enable-identity-sharing",
        description="""Indicates whether Identity Awareness Sharing global use is enabled on the target.""",
    )
    identity_sharing_domains: list[dict] = Field(
        alias="identity-sharing-domains",
        description="""Domains that Identity Awareness Sharing global use applied to them.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
