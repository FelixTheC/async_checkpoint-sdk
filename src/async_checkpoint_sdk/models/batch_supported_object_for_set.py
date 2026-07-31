from pydantic import BaseModel, Field


class BatchSupportedObjectForSet(BaseModel):
    type: str = Field(
        alias="type",
        description="""Type of objects to be updated. <br>Only types from above are supported. Important: the hyphen between address and range must be included in the syntax.""",
    )
    list: list[dict] = Field(
        alias="list",
        description="""List of objects from the same type to be updated. <br>Use the set API reference documentation for a single object command to find the expected fields for the request. <br>For example: to update hosts, use the set-host command found in the API reference documentation (under Network Objects). <br>Note: ignore-errors, ignore-warnings and details-level options are not supported when updating a batch of objects.""",
    )
