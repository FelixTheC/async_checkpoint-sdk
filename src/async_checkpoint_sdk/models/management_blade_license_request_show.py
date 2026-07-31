from .pydantic import BaseModel, Field


class ManagementBladeLicenseRequestShow(BaseModel):
    sku: str | list[str] = Field(alias="sku", description="""N/A""")
