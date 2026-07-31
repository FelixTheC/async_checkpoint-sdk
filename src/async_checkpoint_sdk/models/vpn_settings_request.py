from .pydantic import BaseModel, Field


class VpnSettingsRequest(BaseModel):
    vpn_domain: str = Field(
        alias="vpn-domain",
        description="""Network group representing the customized encryption domain. Must be set when vpn-domain-type is set to 'manual' option.""",
    )
    vpn_domain_exclude_external_ip_addresses: bool = Field(
        alias="vpn-domain-exclude-external-ip-addresses",
        description="""Exclude the external IP addresses from .the VPN domain of this Interoperable Device.""",
    )
    vpn_domain_type: str = Field(
        alias="vpn-domain-type", description="""Indicates the encryption domain."""
    )
