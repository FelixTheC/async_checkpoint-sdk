from .pydantic import BaseModel, Field


class CustomSummaryFieldsReply(BaseModel):
    field_1: str = Field(alias="field-1", description="""First custom field.""")
    field_2: str = Field(alias="field-2", description="""Second custom field.""")
    field_3: str = Field(alias="field-3", description="""Third custom field.""")
