from pydantic import BaseModel, Field


class SmtpRewriteHeaderRequest(BaseModel):
    original: str = Field(alias="original", description="""Original field.""")
    rewritten: str = Field(alias="rewritten", description="""Replacement field.""")
