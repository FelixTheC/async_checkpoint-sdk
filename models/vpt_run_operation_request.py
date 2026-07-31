from pydantic import BaseModel, Field
from vpt_add_phys_interface_request import VptAddPhysInterfaceRequest
from vpt_add_route_request import VptAddRouteRequest
from vpt_add_vd_interface_request import VptAddVdInterfaceRequest
from vpt_add_vd_request import VptAddVdRequest
from vpt_add_vsx_cluster_request import VptAddVsxClusterRequest
from vpt_add_vsx_gw_request import VptAddVsxGwRequest
from vpt_attach_bridge_request import VptAttachBridgeRequest
from vpt_remove_phys_interface_request import VptRemovePhysInterfaceRequest
from vpt_remove_route_request import VptRemoveRouteRequest
from vpt_remove_vd_interface_request import VptRemoveVdInterfaceRequest
from vpt_remove_vd_request import VptRemoveVdRequest
from vpt_remove_vsx_request import VptRemoveVsxRequest
from vpt_set_phys_interface_request import VptSetPhysInterfaceRequest
from vpt_set_vd_interface_request import VptSetVdInterfaceRequest
from vpt_set_vd_request import VptSetVdRequest


class VptRunOperationRequest(BaseModel):
    add_physical_interface_params: VptAddPhysInterfaceRequest = Field(
        alias="add-physical-interface-params",
        description="""Parameters for the operation to add a physical interface to a VSX gateway or VSX Cluster.""",
    )
    add_route_params: VptAddRouteRequest = Field(
        alias="add-route-params",
        description="""Parameters for the operation to add a route to a Virtual System or Virtual Router.""",
    )
    add_vd_interface_params: VptAddVdInterfaceRequest = Field(
        alias="add-vd-interface-params",
        description="""Parameters for the operation to add a new interface to a Virtual Device.""",
    )
    add_vd_params: VptAddVdRequest = Field(
        alias="add-vd-params",
        description="""Parameters for the operation to add a new Virtual Device (VS/VSB/VSW/VR).""",
    )
    add_vsx_cluster_params: VptAddVsxClusterRequest = Field(
        alias="add-vsx-cluster-params",
        description="""Parameters for the operation to add a new VSX Cluster.""",
    )
    add_vsx_gateway_params: VptAddVsxGwRequest = Field(
        alias="add-vsx-gateway-params",
        description="""Parameters for the operation to add a new VSX Gateway.""",
    )
    attach_bridge_params: VptAttachBridgeRequest = Field(
        alias="attach-bridge-params",
        description="""Parameters for the operation to attach a new bridge interface to a Virtual System.""",
    )
    remove_physical_interface_params: VptRemovePhysInterfaceRequest = Field(
        alias="remove-physical-interface-params",
        description="""Parameters for the operation to remove a physical interface from a VSX (Gateway or Cluster).""",
    )
    remove_route_params: VptRemoveRouteRequest = Field(
        alias="remove-route-params",
        description="""Parameters for the operation to remove a route from a Virtual System or Virtual Router.""",
    )
    remove_vd_interface_params: VptRemoveVdInterfaceRequest = Field(
        alias="remove-vd-interface-params",
        description="""Parameters for the operation to remove a logical interface from a Virtual Device.""",
    )
    remove_vd_params: VptRemoveVdRequest = Field(
        alias="remove-vd-params",
        description="""Parameters for the operation to remove a Virtual Device.""",
    )
    remove_vsx_params: VptRemoveVsxRequest = Field(
        alias="remove-vsx-params",
        description="""Parameters for the operation to remove a VSX Gateway or VSX Cluster.""",
    )
    set_physical_interface_params: VptSetPhysInterfaceRequest = Field(
        alias="set-physical-interface-params",
        description="""Parameters for the operation to change the configuration of a physical interface.""",
    )
    set_vd_interface_params: VptSetVdInterfaceRequest = Field(
        alias="set-vd-interface-params",
        description="""Parameters for the operation to change the configuration of a logical interface.""",
    )
    set_vd_params: VptSetVdRequest = Field(
        alias="set-vd-params",
        description="""Parameters for the operation to change the configuration of a Virtual Device.""",
    )
