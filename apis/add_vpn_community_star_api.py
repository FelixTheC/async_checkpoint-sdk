from config import Config
from aiohttp import ClientSession
from models.vpn_star_community_reply import VpnStarCommunityReply
from models.vpn_star_community_request_new import VpnStarCommunityRequestNew


async def add_vpn_community_star(
    client: ClientSession, data: VpnStarCommunityRequestNew, config: Config, **kwargs
) -> VpnStarCommunityReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VpnStarCommunityRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VpnStarCommunityReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-vpn-community-star"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VpnStarCommunityReply(**resp)
