from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class GatewayGlobalUseRequestSet(BaseModel):
    enable_vpn: bool = Field(
        alias="enable-vpn",
        description="""Indicates whether VPN global use is enabled on the target.""",
    )
    enable_identity_sharing: bool = Field(
        alias="enable-identity-sharing",
        description="""Indicates whether Identity Awareness Sharing global use is enabled on the target.""",
    )
    identity_sharing_domains: add | remove | str | list[str] = Field(
        alias="identity-sharing-domains",
        description="""Domains that Identity Awareness Sharing global use applied to them (target domain will be added implicitly if not part of the list).""",
    )
