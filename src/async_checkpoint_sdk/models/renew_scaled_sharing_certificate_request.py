from pydantic import BaseModel, Field


class RenewScaledSharingCertificateRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Gateway or cluster unique identifier.""")
