from aiohttp import ClientSession

from async_checkpoint_sdk.models.vpn_meshed_community_reply import VpnMeshedCommunityReply
from async_checkpoint_sdk.models.vpn_meshed_community_request_new import (
    VpnMeshedCommunityRequestNew,
)
from config import Config


async def add_vpn_community_meshed(
    client: ClientSession, data: VpnMeshedCommunityRequestNew, config: Config, **kwargs
) -> VpnMeshedCommunityReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : VpnMeshedCommunityRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VpnMeshedCommunityReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-vpn-community-meshed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VpnMeshedCommunityReply(**resp)
