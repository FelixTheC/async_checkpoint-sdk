from pydantic import BaseModel, Field


class ViewCentralLicensesListReply(BaseModel):
    licenses_usage: list[dict] = Field(
        alias="licenses-usage", description="""A list containing the attached licenses."""
    )
