from .pydantic import BaseModel, Field


class OverviewObject(BaseModel):
    value: str = Field(alias="##default", description="""N/A""")
