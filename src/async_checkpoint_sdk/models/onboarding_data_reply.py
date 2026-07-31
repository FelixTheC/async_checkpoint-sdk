from .pydantic import BaseModel, Field


class OnboardingDataReply(BaseModel):
    data: str = Field(alias="data", description="""N/A""")
