from .dynamic_object_request_new import DynamicObjectRequestNew
from .lsm_gateway_sic_request import LsmGatewaySicRequest
from .provisioning_settings_request import ProvisioningSettingsRequest
from .pydantic import BaseModel, Field
from .topology_request_new import TopologyRequestNew


class LsmGatewayRequestNew(BaseModel):
    device_id: str = Field(alias="device-id", description="""Device ID.""")
    dynamic_objects: DynamicObjectRequestNew | list[dict] = Field(
        alias="dynamic-objects", description="""Dynamic Objects."""
    )
    provisioning_settings: ProvisioningSettingsRequest = Field(
        alias="provisioning-settings", description="""Provisioning settings."""
    )
    provisioning_state: str = Field(
        alias="provisioning-state",
        description="""Provisioning state. By default the state is 'manual'- enable provisioning but not attach to profile.
If 'using-profile' state is provided a provisioning profile must be provided in provisioning-settings.""",
    )
    sic: LsmGatewaySicRequest = Field(alias="sic", description="""Secure Internal Communication.""")
    topology: TopologyRequestNew = Field(alias="topology", description="""Topology.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings",
        description="""Apply changes ignoring warnings. By Setting this parameter to 'true' SIC failure will be ignored.""",
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
