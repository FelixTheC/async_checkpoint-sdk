from custom_header_request_new import CustomHeaderRequestNew
from pydantic import BaseModel, Field


class IntelligenceFeedToCheckRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    feed_url: str = Field(
        alias="feed-url",
        description="""URL of the feed.
URL should be written as http or https.""",
    )
    action: str = Field(alias="action", description="""The feed indicator's action.""")
    certificate_id: str = Field(
        alias="certificate-id", description="""Certificate SHA-1 fingerprint to access the feed."""
    )
    confidence: int = Field(
        alias="confidence",
        description="""Set in order to configure the confidence of the snort protections in snort format. 1-Low, 5-High.""",
    )
    custom_comment: int = Field(
        alias="custom-comment", description="""Custom IOC feed - the column number of comment."""
    )
    custom_confidence: int = Field(
        alias="custom-confidence",
        description="""Custom IOC feed - the column number of confidence.""",
    )
    custom_header: CustomHeaderRequestNew | list[dict] = Field(
        alias="custom-header", description="""Custom HTTP headers."""
    )
    custom_name: int = Field(
        alias="custom-name", description="""Custom IOC feed - the column number of name."""
    )
    custom_severity: int = Field(
        alias="custom-severity", description="""Custom IOC feed - the column number of severity."""
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
    feed_type: str = Field(alias="feed-type", description="""Feed type to be enforced.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    password: str = Field(
        alias="password", description="""password for authenticating with the URL."""
    )
    performance_impact: int = Field(
        alias="performance-impact",
        description="""Set in order to configure the performance impact of the snort protections in snort format. 1-Very Low, 4-High.""",
    )
    severity: int = Field(
        alias="severity",
        description="""Set in order to configure the severity of the snort protections in snort format. 1-Low, 4-Critical.""",
    )
    use_custom_feed_settings: bool = Field(
        alias="use-custom-feed-settings",
        description="""Set in order to configure a custom indicator feed.""",
    )
    use_snort_format: bool = Field(
        alias="use-snort-format",
        description="""Set in order to configure a snort format indicator feed.""",
    )
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
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
