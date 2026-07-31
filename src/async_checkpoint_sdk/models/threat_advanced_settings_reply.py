from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from resource_classification_reply import ResourceClassificationReply


class ThreatAdvancedSettingsReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
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
    resource_classification: ResourceClassificationReply = Field(
        alias="resource-classification",
        description="""Allow (Background) or Block (Hold) requests until categorization is complete.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions", description="""Actions that are available on the object."""
    )
