from .pydantic import BaseModel, Field


class AccessPointRequestNew(BaseModel):
    enforce_end_user_domain: bool = Field(
        alias="enforce-end-user-domain",
        description="""Enable enforce end user domain.""",
    )
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
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
