from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class AzureADContentObjectReply(BaseModel):
    name_in_azure_ad: str = Field(
        alias="name-in-azure-ad", description="""Object name in the Azure AD."""
    )
    uid_in_azure_ad: str = Field(
        alias="uid-in-azure-ad",
        description="""Unique identifier of the object in the Azure AD.""",
    )
    azure_ad_object: ApiObjectStandardIdentifier = Field(
        alias="azure-ad-object",
        description="""The imported management object (if exists). Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    name: str = Field(alias="name", description="""Object management name.""")
    type_in_azure_ad: str = Field(
        alias="type-in-azure-ad", description="""Object type in Azure AD."""
    )
    additional_properties: list[dict] = Field(
        alias="additional-properties",
        description="""Additional properties on the object.""",
    )
