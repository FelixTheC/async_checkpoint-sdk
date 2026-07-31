from .pydantic import BaseModel, Field


class SmtpRewriteCustomHeaderReply(BaseModel):
    original: str = Field(alias="original", description="""Original field.""")
    rewritten: str = Field(alias="rewritten", description="""Replacement field.""")
    field: str = Field(alias="field", description="""The name of the header.""")
