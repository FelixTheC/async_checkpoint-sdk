from .custom_frequency_settings import CustomFrequencySettings
from .pydantic import BaseModel, Field


class UserCheckRequest(BaseModel):
    confirm: str = Field(alias="confirm", description="""N/A""")
    custom_frequency: CustomFrequencySettings = Field(
        alias="custom-frequency", description="""N/A"""
    )
    frequency: str = Field(alias="frequency", description="""N/A""")
    interaction: str = Field(alias="interaction", description="""N/A""")
