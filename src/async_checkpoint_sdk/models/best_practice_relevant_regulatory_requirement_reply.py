from .pydantic import BaseModel, Field


class BestPracticeRelevantRegulatoryRequirementReply(BaseModel):
    regulation_name: str = Field(
        alias="regulation-name", description="""The name of the regulation."""
    )
    requirement_description: str = Field(
        alias="requirement-description",
        description="""The description of the requirement.""",
    )
    requirement_id: str = Field(
        alias="requirement-id", description="""The id of the requirement."""
    )
    requirement_status: str = Field(
        alias="requirement-status", description="""The status of the requirement."""
    )
    requirement_uid: str = Field(
        alias="requirement-uid",
        description="""The unique identifier of the requirement.""",
    )
