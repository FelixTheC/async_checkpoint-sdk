from pydantic import BaseModel, Field


class ShowCommandsRequest(BaseModel):
    prefix: str = Field(
        alias="prefix", description="""The prefix of the desired commands to show."""
    )
