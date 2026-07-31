from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field
from updatable_object_additional_properties import UpdatableObjectAdditionalProperties


class UpdatableObjectsRepositoryContentObjectReply(BaseModel):
    name_in_updatable_objects_repository: str = Field(
        alias="name-in-updatable-objects-repository",
        description="""Object name in the Updatable Objects Repository.""",
    )
    uid_in_updatable_objects_repository: str = Field(
        alias="uid-in-updatable-objects-repository",
        description="""Unique identifier of the object in the Updatable Objects Repository.""",
    )
    additional_properties: UpdatableObjectAdditionalProperties = Field(
        alias="additional-properties",
        description="""Additional properties on the object.""",
    )
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    updatable_object: ApiObjectStandardIdentifier = Field(
        alias="updatable-object",
        description="""The imported management object (if exists). Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
