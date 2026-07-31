from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class IntelligenceFeedReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    feed_url: str = Field(
        alias="feed-url",
        description="""URL of the feed.
URL should be written as http or https.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    action: str = Field(alias="action", description="""The feed indicator's action.""")
    certificate_id: str = Field(
        alias="certificate-id",
        description="""Certificate SHA-1 fingerprint to access the feed.""",
    )
    confidence: int = Field(alias="confidence", description="""N/A""")
    custom_comment: int = Field(
        alias="custom-comment",
        description="""Custom IOC feed - the column number of comment.""",
    )
    custom_confidence: int = Field(
        alias="custom-confidence",
        description="""Custom IOC feed - the column number of confidence.""",
    )
    custom_headers: list[dict] = Field(
        alias="custom-headers",
        description="""Mapping of column names to column numbers for the configuration of a custom indicator.""",
    )
    custom_name: int = Field(
        alias="custom-name",
        description="""Custom IOC feed - the column number of name.""",
    )
    custom_severity: int = Field(
        alias="custom-severity",
        description="""Custom IOC feed - the column number of severity.""",
    )
    custom_type: int = Field(
        alias="custom-type",
        description="""Custom IOC feed - the column number of type in case a specific type is not chosen.""",
    )
    custom_value: int = Field(
        alias="custom-value",
        description="""Custom IOC feed - the column number of value in case a specific type is chosen.""",
    )
    enabled: bool = Field(
        alias="enabled", description="""Sets whether this indicator feed is enabled."""
    )
    feed_type: str = Field(
        alias="feed-type", description="""Feed type to be enforced."""
    )
    performance_impact: int = Field(alias="performance-impact", description="""N/A""")
    severity: int = Field(alias="severity", description="""N/A""")
    use_custom_feed_settings: bool = Field(
        alias="use-custom-feed-settings",
        description="""Set in order to configure a custom indicator feed.""",
    )
    use_snort_format: bool = Field(alias="use-snort-format", description="""N/A""")
    username: str = Field(
        alias="username", description="""username for authenticating with the URL."""
    )
    fields_delimiter: str = Field(
        alias="fields-delimiter",
        description="""The delimiter that separates between the columns in the feed.""",
    )
    ignore_lines_that_start_with: str = Field(
        alias="ignore-lines-that-start-with",
        description="""A prefix that will determine which lines to ignore.""",
    )
    use_gateway_proxy: bool = Field(
        alias="use-gateway-proxy",
        description="""Use the gateway's proxy for retrieving the feed.""",
    )
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
