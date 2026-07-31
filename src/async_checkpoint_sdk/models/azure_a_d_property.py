from .pydantic import BaseModel, Field


class AzureADProperty(BaseModel):
    name: str = Field(alias="name", description="""N/A""")
    value: str = Field(alias="value", description="""N/A""")
