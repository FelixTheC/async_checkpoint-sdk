from add import Add
from day_recurrence import DayRecurrence
from pydantic import BaseModel, Field
from remove import Remove
from time_object_for_request import TimeObjectForRequest


class TimeRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    end: TimeObjectForRequest = Field(
        alias="end",
        description="""End time. Note: Each gateway may interpret this time differently according to its time zone.""",
    )
    end_never: bool = Field(alias="end-never", description="""End never.""")
    hours_ranges: list[dict] = Field(
        alias="hours-ranges",
        description="""Hours recurrence. List can support up to 3 objects.
Note: Each gateway may interpret this time differently according to its time zone.""",
    )
    new_name: str = Field(
        alias="new-name",
        description="""New name of the Time object. Cannot be more than 11 characters. Should be unique in the domain.""",
    )
    start: TimeObjectForRequest = Field(
        alias="start",
        description="""Starting time. Note: Each gateway may interpret this time differently according to its time zone.""",
    )
    start_now: bool = Field(alias="start-now", description="""Start immediately.""")
    recurrence: DayRecurrence = Field(alias="recurrence", description="""Days recurrence.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: Add | Remove | str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
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
