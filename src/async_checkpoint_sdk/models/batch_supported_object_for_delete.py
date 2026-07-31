from pydantic import BaseModel, Field


class BatchSupportedObjectForDelete(BaseModel):
    type: str = Field(
        alias="type",
        description="""Type of objects to be deleted. <br>Only types from above are supported. Important: the hyphen between address and range must be included in the syntax.""",
    )
    list: list[dict] = Field(
        alias="list",
        description="""List of objects from the same type to be deleted. <br>Use the delete API reference documentation for a single object command to find the expected fields for the request.<br>For example: to delete hosts, use the delete-host command found in the API reference documentation (under Network Objects). <br>Note: ignore-errors, ignore-warnings and details-level options are not supported when deleting a batch of objects.""",
    )
