from pydantic import BaseModel, Field


class RenewScaledSharingCertificateReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
