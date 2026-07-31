from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class DataCenterContentObjectReply(BaseModel):
    name_in_data_center: str = Field(
        alias="name-in-data-center", description="""Object name in the Data Center."""
    )
    uid_in_data_center: str = Field(
        alias="uid-in-data-center",
        description="""Unique identifier of the object in the Data Center.""",
    )
    data_center_object: ApiObjectStandardIdentifier = Field(
        alias="data-center-object",
        description="""The imported management object (if exists). Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    name: str = Field(alias="name", description="""Object management name.""")
    type_in_data_center: str = Field(
        alias="type-in-data-center", description="""Object type in Data Center."""
    )
    additional_properties: list[dict] = Field(
        alias="additional-properties",
        description="""Additional properties on the object.""",
    )
