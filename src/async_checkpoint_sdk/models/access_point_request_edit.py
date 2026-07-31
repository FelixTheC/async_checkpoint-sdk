from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class AccessPointRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    apn: str = Field(alias="apn", description="""APN name.""")
    enforce_end_user_domain: bool = Field(
        alias="enforce-end-user-domain", description="""Enable enforce end user domain."""
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    block_traffic_other_end_user_domains: bool = Field(
        alias="block-traffic-other-end-user-domains",
        description="""Block MS to MS traffic between this and other APN end user domains.""",
    )
    block_traffic_this_end_user_domain: bool = Field(
        alias="block-traffic-this-end-user-domain",
        description="""Block MS to MS traffic within this end user domain.""",
    )
    end_user_domain: str = Field(
        alias="end-user-domain", description="""End user domain name or UID."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: Add | Remove | str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
