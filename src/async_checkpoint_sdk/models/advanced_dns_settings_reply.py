from .pydantic import BaseModel, Field


class AdvancedDnsSettingsReply(BaseModel):
    dga_detection: str = Field(
        alias="dga-detection",
        description="""Enable/Disable DGA based domains detection.""",
    )
    dns_domain_tunneling: str = Field(
        alias="dns-domain-tunneling",
        description="""Enable/Disable DNS Tunneling based on domains detection.""",
    )
    dns_over_https: str = Field(
        alias="dns-over-https",
        description="""Enable/Disable parsing of DNS over HTTPS protocol.""",
    )
    nxns_attack_detection: str = Field(
        alias="nxns-attack-detection",
        description="""Enable/Disable NXNS attack detection.""",
    )
