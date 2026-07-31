from .pydantic import BaseModel, Field


class RevertToRevisionRequest(BaseModel):
    to_session: str = Field(
        alias="to-session",
        description="""Session unique identifier. Specify the session  id you would like to revert your database to.""",
    )
