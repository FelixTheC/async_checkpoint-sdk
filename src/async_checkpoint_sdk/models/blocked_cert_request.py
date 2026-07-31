from .pydantic import BaseModel, Field


class BlockedCertRequest(BaseModel):
    comments: str = Field(
        alias="comments",
        description="""Describes the certificate by default, can be overridden by any text.""",
    )
