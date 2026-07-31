from .pydantic import BaseModel, Field


class ManagementBladeLicenseReply(BaseModel):
    license_data: list[dict] = Field(alias="license-data", description="""N/A""")
