from pydantic import BaseModel, Field


class Range(BaseModel):
    start: str = Field(alias="start", description="""N/A""")
    end: str = Field(alias="end", description="""N/A""")
