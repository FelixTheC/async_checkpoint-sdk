from pydantic import BaseModel, Field


class ManagementBladeTrialLicenseRequest(BaseModel):
    blade: str = Field(alias="blade", description="""N/A""")
