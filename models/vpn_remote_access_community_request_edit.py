from add import add
from participants_domains_request import ParticipantsDomainsRequest
from pydantic import BaseModel, Field
from remove import remove


class VpnRemoteAccessCommunityRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    gateways: add | remove | str | list[str] = Field(
        alias="gateways",
        description="""Collection of VPN Gateway and VPN Device objects identified by the name or UID.""",
    )
    user_groups: add | remove | str | list[str] = Field(
        alias="user-groups",
        description="""Collection of User group objects identified by the name or UID.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    override_vpn_domains: add | remove | ParticipantsDomainsRequest | list[dict] = (
        Field(
            alias="override-vpn-domains",
            description="""The Overrides VPN Domains of the participants GWs.""",
        )
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
