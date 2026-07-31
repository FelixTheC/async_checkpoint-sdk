from .pydantic import BaseModel, Field


class ManagementBladeTrialLicenseShowReply(BaseModel):
    days_until_expiration: int = Field(alias="days-until-expiration", description="""N/A""")
