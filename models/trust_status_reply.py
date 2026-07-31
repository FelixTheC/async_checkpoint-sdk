from pydantic import BaseModel, Field
from trust_details_reply import TrustDetailsReply


class TrustStatusReply(BaseModel):
    sic_message: str = Field(
        alias="sic-message", description="""SIC message from the gateway."""
    )
    sic_name: str = Field(
        alias="sic-name", description="""SIC (Secure Internal Communication) name."""
    )
    sic_status: str = Field(
        alias="sic-status",
        description="""SIC Status reflects the state of the gateway after it has received the certificate issued by the ICA.""",
    )
    trust_details: TrustDetailsReply = Field(
        alias="trust-details", description="""Details for trusted communication."""
    )
