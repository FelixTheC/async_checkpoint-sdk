from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class SendWebRequestActionReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    url: str = Field(alias="url", description="""URL used for the web request.""")
    fingerprint: str = Field(
        alias="fingerprint",
        description="""The SHA1 fingerprint of the URL's SSL certificate. Used to trust servers with self-signed SSL certificates.""",
    )
    override_proxy: bool = Field(
        alias="override-proxy",
        description="""Option to send to the web request via a proxy other than the Management's Server proxy (if defined).""",
    )
    proxy_url: str = Field(
        alias="proxy-url", description="""URL of the proxy used to send the request."""
    )
    shared_secret: str = Field(
        alias="shared-secret",
        description="""Shared secret that can be used by the target server to identify the Management Server.<br>The value will be sent as part of the request in the X-chkp-shared-secret header.""",
    )
    time_out: int = Field(
        alias="time-out", description="""Web Request time-out in seconds."""
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
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
