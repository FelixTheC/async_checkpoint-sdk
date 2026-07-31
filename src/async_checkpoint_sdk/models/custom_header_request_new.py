from pydantic import BaseModel, Field


class CustomHeaderRequestNew(BaseModel):
    header_name: str = Field(
        alias="header-name", description="""The name of the HTTP header we wish to add."""
    )
    header_value: str = Field(
        alias="header-value", description="""The name of the HTTP value we wish to add."""
    )
