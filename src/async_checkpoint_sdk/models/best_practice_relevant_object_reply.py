from pydantic import BaseModel, Field


class BestPracticeRelevantObjectReply(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Determines if the relevant object is enabled or not."""
    )
    name: str = Field(alias="name", description="""The name of the relevant object.""")
    status: str = Field(alias="status", description="""The status of the relevant object.""")
    uid: str = Field(alias="uid", description="""The uid of the relevant object.""")
