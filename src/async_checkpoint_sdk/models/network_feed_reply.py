from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class NetworkFeedReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    feed_url: str = Field(
        alias="feed-url",
        description="""URL of the feed.
URL should be written as http or https.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    certificate_id: str = Field(
        alias="certificate-id", description="""Certificate SHA-1 fingerprint to access the feed."""
    )
    username: str = Field(
        alias="username", description="""username for authenticating with the URL."""
    )
    feed_format: str = Field(alias="feed-format", description="""Feed file format.""")
    feed_type: str = Field(alias="feed-type", description="""Feed type to be enforced.""")
    custom_headers: list[dict] = Field(
        alias="custom-headers",
        description="""Headers to allow different authentication methods with the URL.""",
    )
    update_interval: int = Field(
        alias="update-interval",
        description="""Interval in minutes for updating the feed on the Security Gateway.""",
    )
    data_column: int = Field(
        alias="data-column", description="""Number of the column that contains the feed's data."""
    )
    fields_delimiter: str = Field(
        alias="fields-delimiter",
        description="""The delimiter that separates between the columns in the feed.""",
    )
    ignore_lines_that_start_with: str = Field(
        alias="ignore-lines-that-start-with",
        description="""A prefix that will determine which lines to ignore.""",
    )
    json_query: str = Field(alias="json-query", description="""Json Query to be parsed.""")
    use_gateway_proxy: bool = Field(
        alias="use-gateway-proxy",
        description="""Use the gateway's proxy for retrieving the feed.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
