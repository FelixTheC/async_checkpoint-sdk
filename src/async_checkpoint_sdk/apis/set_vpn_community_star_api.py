from aiohttp import ClientSession

from async_checkpoint_sdk.models.vpn_star_community_reply import VpnStarCommunityReply
from async_checkpoint_sdk.models.vpn_star_community_request_edit import VpnStarCommunityRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_vpn_community_star(
    client: ClientSession, data: VpnStarCommunityRequestEdit, config: SDKConfig, **kwargs
) -> VpnStarCommunityReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : VpnStarCommunityRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VpnStarCommunityReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-vpn-community-star"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VpnStarCommunityReply(**resp)
