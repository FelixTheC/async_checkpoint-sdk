from config import Config
from aiohttp import ClientSession
from models.access_point_request_edit import AccessPointRequestEdit
from models.access_point_reply import AccessPointReply


async def clone_access_point_name(
    client: ClientSession, data: AccessPointRequestEdit, config: Config, **kwargs
) -> AccessPointReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessPointRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessPointReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-access-point-name"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessPointReply(**resp)
