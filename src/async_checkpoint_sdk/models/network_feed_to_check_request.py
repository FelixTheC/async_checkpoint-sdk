from custom_header_request_new import CustomHeaderRequestNew
from pydantic import BaseModel, Field


class NetworkFeedToCheckRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    feed_url: str = Field(
        alias="feed-url",
        description="""URL of the feed.
URL should be written as http or https.""",
    )
    certificate_id: str = Field(
        alias="certificate-id", description="""Certificate SHA-1 fingerprint to access the feed."""
    )
    feed_format: str = Field(alias="feed-format", description="""Feed file format.""")
    feed_type: str = Field(alias="feed-type", description="""Feed type to be enforced.""")
    password: str = Field(
        alias="password", description="""password for authenticating with the URL."""
    )
    username: str = Field(
        alias="username", description="""username for authenticating with the URL."""
    )
    custom_header: CustomHeaderRequestNew | list[dict] = Field(
        alias="custom-header",
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
    json_query: str = Field(alias="json-query", description="""JQ query to be parsed.""")
    use_gateway_proxy: bool = Field(
        alias="use-gateway-proxy",
        description="""Use the gateway's proxy for retrieving the feed.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
