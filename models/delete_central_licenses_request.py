from pydantic import BaseModel, Field


class DeleteCentralLicensesRequest(BaseModel):
    signature: str = Field(
        alias="signature", description="""The license's signature to be deleted."""
    )
