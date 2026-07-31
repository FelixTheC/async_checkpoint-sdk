from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class GatewayGlobalUseRequestSet(BaseModel):
    target: str = Field(
        alias="target",
        description="""On what target to execute this command. Target may be identified by its object name, or object unique identifier.""",
    )
    enable_vpn: bool = Field(
        alias="enable-vpn",
        description="""Indicates whether VPN global use is enabled on the target.""",
    )
    enable_identity_sharing: bool = Field(
        alias="enable-identity-sharing",
        description="""Indicates whether Identity Awareness Sharing global use is enabled on the target.""",
    )
    identity_sharing_domains: Add | Remove | str | list[str] = Field(
        alias="identity-sharing-domains",
        description="""Domains that Identity Awareness Sharing global use applied to them (target domain will be added implicitly if not part of the list).""",
    )
