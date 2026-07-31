from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class TaskEntityReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    last_update_time: ApiDateReply = Field(
        alias="last-update-time", description="""N/A"""
    )
    progress_description: str = Field(
        alias="progress-description", description="""N/A"""
    )
    progress_percentage: int = Field(alias="progress-percentage", description="""N/A""")
    revert_status: str = Field(alias="revert-status", description="""N/A""")
    start_time: ApiDateReply = Field(alias="start-time", description="""N/A""")
    status: str = Field(alias="status", description="""Task status.""")
    suppressed: bool = Field(alias="suppressed", description="""N/A""")
    task_details: list[dict] = Field(
        alias="task-details",
        description="""Task-specific details according to the requested task type.""",
    )
    task_id: str = Field(
        alias="task-id",
        description="""Asynchronous task unique identifier. Use show-task command to check the progress of the task.""",
    )
    task_name: str = Field(alias="task-name", description="""N/A""")
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
