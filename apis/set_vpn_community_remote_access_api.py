from config import Config
from aiohttp import ClientSession
from models.vpn_remote_access_community_request_edit import VpnRemoteAccessCommunityRequestEdit
from models.vpn_remote_access_community_reply import VpnRemoteAccessCommunityReply


async def set_vpn_community_remote_access(
    client: ClientSession, data: VpnRemoteAccessCommunityRequestEdit, config: Config, **kwargs
) -> VpnRemoteAccessCommunityReply:
    """
    Edit existing Remote Access object. Using object name or uid is optional. </br>Add and Delete API commands for this object are unavailable since there is single object per domain.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VpnRemoteAccessCommunityRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VpnRemoteAccessCommunityReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-vpn-community-remote-access"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VpnRemoteAccessCommunityReply(**resp)
