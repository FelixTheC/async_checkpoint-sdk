from pydantic import BaseModel, Field


class RuleBatchSupportedObjectForDelete(BaseModel):
    layer: str = Field(alias="layer", description="""Layer name or uid.""")
    type: str = Field(
        alias="type",
        description="""Type of rules to be deleted. <br>Only types from above are supported.""",
    )
    list: list[dict] = Field(
        alias="list",
        description="""List of rules from the same type to be deleted. <br>Use the delete API reference documentation for a single rule command to find the expected fields for the request.<br>For example: to delete access-rule, use the delete-access-rule command found in the API reference documentation (under Access Control & NAT). <br>Note: ignore-errors, ignore-warnings and details-level options are not supported when deleting a batch of objects.""",
    )
