from .pydantic import BaseModel, Field


class TurnOnOffCentralLicensesRequest(BaseModel):
    state: str = Field(alias="state", description="""N/A""")
