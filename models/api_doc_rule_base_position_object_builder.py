from pydantic import BaseModel, Field


class ApiDocRuleBasePositionObjectBuilder(BaseModel):
    top: str = Field(
        alias="top",
        description="""Add rule on top of specific section identified by uid or name""",
    )
