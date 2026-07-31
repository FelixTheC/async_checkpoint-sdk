from pydantic import BaseModel, Field


class ShowHaStateReply(BaseModel):
    domains: list[dict] = Field(alias="domains", description="""Domain servers.""")
