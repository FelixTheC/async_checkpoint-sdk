from add import add
from pydantic import BaseModel, Field
from remove import remove


class DnsDomainRequestEdit(BaseModel):
    is_sub_domain: bool = Field(
        alias="is-sub-domain",
        description="""Whether to match sub-domains in addition to the domain itself.<br>false - Configures the object with the FQDN.<br>true - Configures the object without the FQDN.""",
    )
    new_name: str = Field(
        alias="new-name",
        description="""New name of the DNS domain. Should always start with a '.' character. Should be unique in the domain.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
