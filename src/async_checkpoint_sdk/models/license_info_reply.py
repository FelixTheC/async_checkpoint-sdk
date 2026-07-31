from pydantic import BaseModel, Field


class LicenseInfoReply(BaseModel):
    pool: str = Field(
        alias="pool",
        description="""The pool type is defined by the blades contained in the licenses of this pool.""",
    )
    quota_unit: str = Field(alias="quota-unit", description="""The unit of the quota.""")
    quota_value: str = Field(
        alias="quota-value",
        description="""The number of virtual cores the license covers, as specified when purchased.""",
    )
    type: str = Field(alias="type", description="""The typ of the license.""")
