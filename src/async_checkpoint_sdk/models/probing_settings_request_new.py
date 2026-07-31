from .pydantic import BaseModel, Field


class ProbingSettingsRequestNew(BaseModel):
    probed_interfaces: str = Field(
        alias="probed-interfaces",
        description="""Specifies whether to probe all addresses defined in the topology tab or specific addresses.""",
    )
    probed_interface_list: str | list[str] = Field(
        alias="probed-interface-list",
        description="""List of specific IP addresses to probe. Only relevant when probed-interfaces is set to 'specific'.""",
    )
    use_primary_address: bool = Field(
        alias="use-primary-address",
        description="""Whether to use a primary address for high availability probing.""",
    )
    primary_address: str = Field(
        alias="primary-address",
        description="""Primary IP address to use. Must be one of the addresses from .probed-interface-list. Required when use-primary-address is true.""",
    )
    probing_method: str = Field(
        alias="probing-method",
        description="""Probing method: 'ongoing' for continuous probing or 'one-time' for single probe.""",
    )
