from cpuuid import CPUUID
from pydantic import BaseModel, Field


class CpmiOwned(BaseModel):
    value: CPUUID = Field(alias="##default", description="""N/A""")
