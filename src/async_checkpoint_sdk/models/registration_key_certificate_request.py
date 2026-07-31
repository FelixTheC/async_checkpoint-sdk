from .pydantic import BaseModel, Field


class RegistrationKeyCertificateRequest(BaseModel):
    comment: str = Field(alias="comment", description="""Certificate comment.""")
    expiration_days: int = Field(
        alias="expiration-days", description="""Days which users must to enroll."""
    )
