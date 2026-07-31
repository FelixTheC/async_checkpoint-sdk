from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from day_recurrence import DayRecurrence
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from time_object import TimeObject


class TimeReply(BaseModel):
    name: str = Field(
        alias="name",
        description="""Time object name. Cannot be more than 11 characters. Should be unique in the domain.""",
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    end: TimeObject = Field(
        alias="end",
        description="""End time. Note: Each gateway may interpret this time differently according to its time zone.""",
    )
    end_never: bool = Field(alias="end-never", description="""End never.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    hours_ranges: list[dict] = Field(
        alias="hours-ranges",
        description="""Hours recurrence. List can support up to 3 objects.
Note: Each gateway may interpret this time differently according to its time zone.""",
    )
    start: TimeObject = Field(
        alias="start",
        description="""Starting time. Note: Each gateway may interpret this time differently according to its time zone.""",
    )
    start_now: bool = Field(alias="start-now", description="""Start immediately.""")
    recurrence: DayRecurrence = Field(
        alias="recurrence", description="""Days recurrence."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
