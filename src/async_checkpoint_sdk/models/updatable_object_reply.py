from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from remote_updatable_object_meta_data import RemoteUpdatableObjectMetaData
from updatable_object_additional_properties import UpdatableObjectAdditionalProperties


class UpdatableObjectReply(BaseModel):
    name_in_updatable_objects_repository: str = Field(
        alias="name-in-updatable-objects-repository",
        description="""Object name in the Updatable Objects Repository.""",
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    uid_in_updatable_objects_repository: str = Field(
        alias="uid-in-updatable-objects-repository",
        description="""Unique identifier of the object in the Updatable Objects Repository.""",
    )
    additional_properties: UpdatableObjectAdditionalProperties = Field(
        alias="additional-properties", description="""Additional properties on the object."""
    )
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    updatable_object_meta_info: RemoteUpdatableObjectMetaData = Field(
        alias="updatable-object-meta-info", description="""N/A"""
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
