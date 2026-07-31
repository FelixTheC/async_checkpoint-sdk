from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class OverrideCategorizationReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    url: str = Field(
        alias="url",
        description="""The URL for which we want to update the category and risk definitions, the URL and the object name are the same for Override Categorization.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    url_defined_as_regular_expression: bool = Field(
        alias="url-defined-as-regular-expression",
        description="""States whether the URL is defined as a Regular Expression or not.""",
    )
    new_primary_category: ApiObjectStandardIdentifier = Field(
        alias="new-primary-category",
        description="""Each application is assigned to one primary category based on its most defining aspect.""",
    )
    risk: str = Field(
        alias="risk", description="""States the override categorization risk."""
    )
    additional_categories: list[dict] = Field(
        alias="additional-categories",
        description="""Uid or name of the categories to override in the Application and URL Filtering or Threat Prevention.""",
    )
    comment: str = Field(
        alias="comment", description="""Comment for the categorization override."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
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
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
