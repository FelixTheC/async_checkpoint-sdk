from pydantic import BaseModel, Field


class ZeroPhishingFqdnSettingsReply(BaseModel):
    gateway_fqdn_mode: str = Field(
        alias="gateway-fqdn-mode", description="""Manual Fqdn."""
    )
    manual_fqdn: str = Field(
        alias="manual-fqdn", description="""Zero Phishing gateway FQDN."""
    )
