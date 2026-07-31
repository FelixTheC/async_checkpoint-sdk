from .pydantic import BaseModel, Field


class TurnOnOffCentralLicensesReply(BaseModel):
    status: str = Field(alias="status", description="""N/A""")
