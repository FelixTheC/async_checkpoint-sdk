from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level import MetaInfoForTopLevel
from pydantic import BaseModel, Field


class AdMachineReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    accountunituid: str = Field(alias="accountUnitUid", description="""N/A""")
    additionalattributes: list[dict] = Field(
        alias="additionalAttributes", description="""N/A"""
    )
    customfields: list[dict] = Field(alias="customFields", description="""N/A""")
    display_name: str = Field(alias="display-name", description="""N/A""")
    dn: str = Field(alias="dn", description="""N/A""")
    meta_info: MetaInfoForTopLevel = Field(alias="meta-info", description="""N/A""")
    source: str = Field(
        alias="source",
        description="""Active Directory name or Identity Tag  or Internal User Groups or LDAP Groups or Guests.""",
    )
    tooltiptext: str = Field(alias="tooltiptext", description="""N/A""")
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
