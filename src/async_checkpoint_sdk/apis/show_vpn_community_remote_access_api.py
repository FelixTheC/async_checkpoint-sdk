from aiohttp import ClientSession

from async_checkpoint_sdk.models.vpn_remote_access_community_reply import (
    VpnRemoteAccessCommunityReply,
)
from async_checkpoint_sdk.models.vpn_remote_access_community_request_show import (
    VpnRemoteAccessCommunityRequestShow,
)
from config import Config


async def show_vpn_community_remote_access(
    client: ClientSession, data: VpnRemoteAccessCommunityRequestShow, config: Config, **kwargs
) -> VpnRemoteAccessCommunityReply:
    """
    Retrieve existing Remote Access object. Using object name or uid is optional.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : VpnRemoteAccessCommunityRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VpnRemoteAccessCommunityReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-vpn-community-remote-access"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VpnRemoteAccessCommunityReply(**resp)
