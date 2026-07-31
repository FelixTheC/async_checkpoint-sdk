from pydantic import BaseModel, Field


class AlternateNamesRequest(BaseModel):
    name_type: str = Field(alias="name-type", description="""Alternate name type.""")
    value: str = Field(alias="value", description="""Alternate name value.""")
