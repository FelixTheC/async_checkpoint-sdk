from .cpuuid import CPUUID
from .pydantic import BaseModel, Field


class CustomFieldValue(BaseModel):
    value: CPUUID = Field(alias="##default", description="""N/A""")
