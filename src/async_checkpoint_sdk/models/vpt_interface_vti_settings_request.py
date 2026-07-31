from pydantic import BaseModel, Field


class VptInterfaceVtiSettingsRequest(BaseModel):
    local_ipv4_address: str = Field(
        alias="local-ipv4-address",
        description="""The IPv4 address of the VPN tunnel on this Virtual System.""",
    )
    peer_name: str = Field(
        alias="peer-name",
        description="""The name of the remote peer object as defined in the VPN community.""",
    )
    remote_ipv4_address: str = Field(
        alias="remote-ipv4-address",
        description="""The IPv4 address of the VPN tunnel on the remote VPN peer.""",
    )
    tunnel_id: str = Field(
        alias="tunnel-id",
        description="""Optional unique Tunnel ID.<br/>Automatically assigned by the system if empty.""",
    )
