from pydantic import BaseModel, Field


class BatchSupportedObjectForAdd(BaseModel):
    type: str = Field(
        alias="type",
        description="""Type of objects to be created. <br>Only types from above are supported. Important: the hyphen between address and range must be included in the syntax.""",
    )
    list: list[dict] = Field(
        alias="list",
        description="""List of objects from the same type to be created. <br>Use the add API reference documentation for a single object command to find the expected fields for the request. <br>For example: to add hosts, use the add-host command found in the API reference documentation (under Network Objects). <br>Note: Set-if-exists, ignore-errors, ignore-warnings and details-level options are not supported when adding a batch of objects.""",
    )
