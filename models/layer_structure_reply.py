from api_domain_identifier import ApiDomainIdentifier
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from root_section_reply import RootSectionReply


class LayerStructureReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    root_section: RootSectionReply = Field(
        alias="root-section", description="""Root layer section."""
    )
    place_holder: str = Field(
        alias="place-holder",
        description="""Place holder unique identifier. This field is relevant on Multi Domain environments with global domain assignment. See 'show-place-holder' command.""",
    )
    source: int = Field(
        alias="from", description="""From which element number the query was done."""
    )
    to: int = Field(
        alias="to", description="""To which element number the query was done."""
    )
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
