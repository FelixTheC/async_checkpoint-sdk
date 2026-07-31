from .pydantic import BaseModel, Field


class WorkSessionRequestShow(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
    detailed_admin_info: bool = Field(
        alias="detailed-admin-info",
        description="""Show the connected Administrator's info in detail.""",
    )
