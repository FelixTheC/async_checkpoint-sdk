from .pydantic import BaseModel, Field


class GetInterfacesRequest(BaseModel):
    group_interfaces_by_subnet: bool = Field(
        alias="group-interfaces-by-subnet",
        description="""Specify whether to group the cluster interfaces by a subnet.
Otherwise, group the cluster interfaces by their names.""",
    )
    use_defined_by_routes: bool = Field(
        alias="use-defined-by-routes",
        description="""Specify whether to configure the topology Defined by Routes where applicable.
Otherwise, configure the topology to This Network as default for internal interfaces.""",
    )
    with_topology: bool = Field(
        alias="with-topology",
        description="""Specify whether to fetch the interfaces with their topology. Otherwise, the Management Server fetches the interfaces without their topology.""",
    )
