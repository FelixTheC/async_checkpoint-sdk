from .pydantic import BaseModel, Field


class PnpLicenseReply(BaseModel):
    days_until_expiration: int = Field(alias="days-until-expiration", description="""N/A""")
