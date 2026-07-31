from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .data_center_server_reply import DataCenterServerReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field
from .remote_data_center_object_meta_data import RemoteDataCenterObjectMetaData


class DataCenterObjectReply(BaseModel):
    name: str = Field(alias="name", description="""Object management name.""")
    name_in_data_center: str = Field(
        alias="name-in-data-center", description="""Object name in the Data Center."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    uid_in_data_center: str = Field(
        alias="uid-in-data-center",
        description="""Unique identifier of the object in the Data Center.""",
    )
    data_center: DataCenterServerReply = Field(
        alias="data-center", description="""The Data Center the object is on."""
    )
    data_center_object_meta_info: RemoteDataCenterObjectMetaData = Field(
        alias="data-center-object-meta-info", description="""N/A"""
    )
    deleted: bool = Field(
        alias="deleted",
        description="""Indicates if the object is inaccessible or deleted on Data Center Server.""",
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    type_in_data_center: str = Field(
        alias="type-in-data-center", description="""Object type in Data Center."""
    )
    additional_properties: list[dict] = Field(
        alias="additional-properties",
        description="""Additional properties on the object.""",
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
