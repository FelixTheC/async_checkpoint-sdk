from pydantic import BaseModel, Field


class WorkSessionPurgeRequest(BaseModel):
    number_of_sessions_to_preserve: int = Field(
        alias="number-of-sessions-to-preserve",
        description="""The number of newest sessions to preserve, by the sessions's publish date.""",
    )
