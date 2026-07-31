from pydantic import BaseModel, Field


class VpnCertificateRequest(BaseModel):
    stored_at: str = Field(
        alias="stored-at",
        description="""Store keys on Security Management Server or on the Gateway. Default value is management server. On cluster object only management server is valid.""",
    )
