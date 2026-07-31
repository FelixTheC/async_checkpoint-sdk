from .pydantic import BaseModel, Field


class CentralLicensesListReply(BaseModel):
    licenses: list[dict] = Field(
        alias="licenses", description="""A list containing the attached licenses."""
    )
