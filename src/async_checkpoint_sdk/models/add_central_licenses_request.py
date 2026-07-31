from pydantic import BaseModel, Field


class AddCentralLicensesRequest(BaseModel):
    license: str = Field(
        alias="license",
        description="""The license string received from the User Center - without 'cplic put'.""",
    )
