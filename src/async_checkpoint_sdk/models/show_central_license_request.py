from pydantic import BaseModel, Field


class ShowCentralLicenseRequest(BaseModel):
    signature: str = Field(alias="signature", description="""The license's signature.""")
