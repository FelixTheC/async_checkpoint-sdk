from pydantic import BaseModel, Field


class VerifyRevertRequest(BaseModel):
    to_session: str = Field(
        alias="to-session",
        description="""Session unique identifier. Specify the session you would like to verify a revert operation to.""",
    )
