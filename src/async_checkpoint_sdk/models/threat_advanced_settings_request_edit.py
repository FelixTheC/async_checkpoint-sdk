from .pydantic import BaseModel, Field
from .resource_classification_request import ResourceClassificationRequest


class ThreatAdvancedSettingsRequestEdit(BaseModel):
    feed_retrieving_interval: str = Field(
        alias="feed-retrieving-interval",
        description="""Feed retrieving intervals of External Feed, in the form of HH:MM.""",
    )
    httpi_non_standard_ports: bool = Field(
        alias="httpi-non-standard-ports",
        description="""Enable HTTP Inspection on non standard ports for Threat Prevention blades.""",
    )
    internal_error_fail_mode: str = Field(
        alias="internal-error-fail-mode",
        description="""In case of internal system error, allow or block all connections.""",
    )
    log_unification_timeout: int = Field(
        alias="log-unification-timeout",
        description="""Session unification timeout for logs (minutes).""",
    )
    resource_classification: ResourceClassificationRequest = Field(
        alias="resource-classification",
        description="""Allow (Background) or Block (Hold) requests until categorization is complete.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
