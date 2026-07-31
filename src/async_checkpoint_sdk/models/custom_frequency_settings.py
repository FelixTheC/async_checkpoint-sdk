from .pydantic import BaseModel, Field


class CustomFrequencySettings(BaseModel):
    every: int = Field(alias="every", description="""N/A""")
    unit: str = Field(alias="unit", description="""N/A""")
