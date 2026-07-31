from api_date_reply import ApiDateReply
from pydantic import BaseModel, Field


class ValidationIncidentReply(BaseModel):
    creation_time: ApiDateReply = Field(alias="creation-time", description="""Creation time.""")
    current_session: bool = Field(
        alias="current-session", description="""Validation related to the current session."""
    )
    message: str = Field(alias="message", description="""Validation message.""")
    name: str = Field(alias="name", description="""Validation name.""")
    related_objects: list[dict] = Field(alias="related-objects", description="""Related objects.""")
