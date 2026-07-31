from custom_frequency_settings import CustomFrequencySettings
from pydantic import BaseModel, Field


class UserCheckReply(BaseModel):
    confirm: str = Field(alias="confirm", description="""N/A""")
    custom_frequency: CustomFrequencySettings = Field(
        alias="custom-frequency", description="""N/A"""
    )
    frequency: str = Field(alias="frequency", description="""N/A""")
    interaction: list[dict] = Field(
        alias="interaction",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
