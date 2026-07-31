from .pydantic import BaseModel, Field


class HostCkpManagementBladesReply(BaseModel):
    network_policy_management: bool = Field(
        alias="network-policy-management",
        description="""Network Policy Management enabled.""",
    )
    secondary: bool = Field(alias="secondary", description="""Secondary Management enabled.""")
    logging_and_status: bool = Field(
        alias="logging-and-status", description="""Logging & Status enabled."""
    )
    endpoint_policy: bool = Field(
        alias="endpoint-policy", description="""Endpoint Policy enabled."""
    )
    identity_logging: bool = Field(
        alias="identity-logging", description="""Identity Logging enabled."""
    )
    smart_event_correlation: bool = Field(
        alias="smart-event-correlation",
        description="""SmartEvent Correlation Unit enabled.""",
    )
    smart_event_server: bool = Field(
        alias="smart-event-server", description="""SmartEvent Server enabled."""
    )
    compliance: bool = Field(alias="compliance", description="""Compliance blade enabled.""")
    user_directory: bool = Field(alias="user-directory", description="""User Directory enabled.""")
