from pydantic import BaseModel, Field


class SharedSecretRequest(BaseModel):
    external_gateway: str = Field(
        alias="external-gateway",
        description="""External gateway identified by the name or UID.""",
    )
    shared_secret: str = Field(alias="shared-secret", description="""Shared secret.""")
