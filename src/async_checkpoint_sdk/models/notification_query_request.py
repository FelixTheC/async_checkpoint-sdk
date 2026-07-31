from .pydantic import BaseModel, Field


class NotificationQueryRequest(BaseModel):
    start_sequence_number: int = Field(alias="start-sequence-number", description="""N/A""")
