from pydantic import BaseModel, Field


class PurgeSamFileReply(BaseModel):
    enabled: bool = Field(alias="enabled", description="""Purge SAM File.""")
    purge_when_size_reaches_to: int = Field(
        alias="purge-when-size-reaches-to", description="""Purge SAM File When it Reaches to."""
    )
