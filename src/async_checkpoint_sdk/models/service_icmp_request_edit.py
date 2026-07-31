from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class ServiceIcmpRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    icmp_code: int = Field(
        alias="icmp-code",
        description="""As listed in: <a href=http://www.iana.org/assignments/icmp-parameters target=_blank>RFC 792</a>.""",
    )
    icmp_type: int = Field(
        alias="icmp-type",
        description="""As listed in: <a href=http://www.iana.org/assignments/icmp-parameters target=_blank>RFC 792</a>.""",
    )
    keep_connections_open_after_policy_installation: bool = Field(
        alias="keep-connections-open-after-policy-installation",
        description="""Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
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
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
