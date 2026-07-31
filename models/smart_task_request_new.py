from pydantic import BaseModel, Field


class SmartTaskRequestNew(BaseModel):
    custom_data: str = Field(
        alias="custom-data",
        description="""Per SmartTask custom data in JSON format.<br>When the trigger is fired, the trigger data is converted to JSON. The custom data is then concatenated to the trigger data JSON.""",
    )
    description: str = Field(
        alias="description",
        description="""Description of the SmartTask's functionality and options.""",
    )
    enabled: bool = Field(
        alias="enabled",
        description="""Whether the SmartTask is enabled and will run when triggered.""",
    )
    fail_open: bool = Field(
        alias="fail-open",
        description="""If the action fails to execute, whether to treat the execution failure as an error, or continue.""",
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
