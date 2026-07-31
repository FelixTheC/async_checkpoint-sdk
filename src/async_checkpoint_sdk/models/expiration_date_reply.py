from date import Date
from pydantic import BaseModel, Field


class ExpirationDateReply(BaseModel):
    expiration_date: Date = Field(alias="expiration-date", description="""Expiration date.""")
    expired: bool = Field(alias="expired", description="""Expired rule.""")
    has_expiration_date: bool = Field(
        alias="has-expiration-date", description="""Rule has expiration date."""
    )
