from pydantic import BaseModel, Field


class HostCkpManagementBladesRequest(BaseModel):
    network_policy_management: bool = Field(
        alias="network-policy-management", description="""Enable Network Policy Management."""
    )
    logging_and_status: bool = Field(
        alias="logging-and-status", description="""Enable Logging & Status."""
    )
    smart_event_server: bool = Field(
        alias="smart-event-server",
        description="""Enable SmartEvent server. </br>When activating SmartEvent server, blades 'logging-and-status' and 'smart-event-correlation' should be set to True. </br>To complete SmartEvent configuration, perform Install Database or Install Policy on your Security Management servers and Log servers. </br>Activating SmartEvent Server is not recommended in Management High Availability environment. For more information refer to sk25164.""",
    )
    smart_event_correlation: bool = Field(
        alias="smart-event-correlation", description="""Enable SmartEvent Correlation Unit."""
    )
    endpoint_policy: bool = Field(
        alias="endpoint-policy",
        description="""Enable Endpoint Policy. </br>To complete Endpoint Security Management configuration, perform Install Database on your Endpoint Management Server. </br>Field is not supported on Multi Domain Server environment.""",
    )
    compliance: bool = Field(
        alias="compliance",
        description="""Compliance blade. Can be set when 'network-policy-management' was selected to be True.""",
    )
    user_directory: bool = Field(
        alias="user-directory",
        description="""Enable User Directory. Can be set when 'network-policy-management' was selected to be True.""",
    )
