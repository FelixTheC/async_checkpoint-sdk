from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from smart_task_action_reply import SmartTaskActionReply


class SmartTaskReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    trigger: ApiObjectStandardIdentifier = Field(
        alias="trigger", description="""Trigger type associated with the SmartTask."""
    )
    type: str = Field(alias="type", description="""Object type.""")
    action: SmartTaskActionReply = Field(
        alias="action", description="""The action to be run when the trigger is fired."""
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
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
