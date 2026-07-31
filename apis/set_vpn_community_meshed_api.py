from config import Config
from aiohttp import ClientSession
from models.vpn_meshed_community_reply import VpnMeshedCommunityReply
from models.vpn_meshed_community_request_edit import VpnMeshedCommunityRequestEdit


async def set_vpn_community_meshed(
    client: ClientSession, data: VpnMeshedCommunityRequestEdit, config: Config, **kwargs
) -> VpnMeshedCommunityReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VpnMeshedCommunityRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VpnMeshedCommunityReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-vpn-community-meshed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VpnMeshedCommunityReply(**resp)
