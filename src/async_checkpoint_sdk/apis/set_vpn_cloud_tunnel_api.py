from aiohttp import ClientSession

from async_checkpoint_sdk.models.vpn_cloud_tunnel_reply import VpnCloudTunnelReply
from async_checkpoint_sdk.models.vpn_cloud_tunnel_request import VpnCloudTunnelRequest
from config import Config


async def set_vpn_cloud_tunnel(
    client: ClientSession, data: VpnCloudTunnelRequest, config: Config, **kwargs
) -> VpnCloudTunnelReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VpnCloudTunnelRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VpnCloudTunnelReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-vpn-cloud-tunnel"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VpnCloudTunnelReply(**resp)
