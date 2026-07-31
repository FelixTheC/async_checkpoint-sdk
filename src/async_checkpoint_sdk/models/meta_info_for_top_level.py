from .date import Date
from .pydantic import BaseModel, Field


class MetaInfoForTopLevel(BaseModel):
    value: Date = Field(alias="##default", description="""N/A""")
