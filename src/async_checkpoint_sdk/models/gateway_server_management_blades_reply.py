from .pydantic import BaseModel, Field


class GatewayServerManagementBladesReply(BaseModel):
    endpoint_policy: bool = Field(alias="endpoint-policy", description="""Endpoint policy blade.""")
    identity_logging: bool = Field(
        alias="identity-logging", description="""Identity logging blade."""
    )
    logging_and_status: bool = Field(
        alias="logging-and-status", description="""Logging & Status blade."""
    )
    network_policy_management: bool = Field(
        alias="network-policy-management",
        description="""Network policy management blade.""",
    )
    secondary: bool = Field(alias="secondary", description="""Secondary blade.""")
    compliance: bool = Field(alias="compliance", description="""Compliance blade.""")
    identity_awareness: bool = Field(
        alias="identity-awareness", description="""Identity awareness blade."""
    )
    monitoring: bool = Field(alias="monitoring", description="""Monitoring blade.""")
    smart_event_correlation: bool = Field(
        alias="smart-event-correlation", description="""SmartEvent correlation blade."""
    )
    smart_event_server: bool = Field(
        alias="smart-event-server", description="""SmartEvent server blade."""
    )
