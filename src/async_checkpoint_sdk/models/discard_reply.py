from .pydantic import BaseModel, Field


class DiscardReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
    number_of_discarded_changes: int = Field(
        alias="number-of-discarded-changes",
        description="""Number of discarded changes.""",
    )
