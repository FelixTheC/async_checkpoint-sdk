from add import Add
from pydantic import BaseModel, Field
from remove import Remove
from smart_task_action_request import SmartTaskActionRequest


class SmartTaskRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    action: SmartTaskActionRequest = Field(
        alias="action", description="""The action to be run when the trigger is fired."""
    )
    trigger: str = Field(
        alias="trigger", description="""Trigger type associated with the SmartTask."""
    )
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
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
