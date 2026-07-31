from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_point_reply import AccessPointReply
from async_checkpoint_sdk.models.access_point_request_new import AccessPointRequestNew
from config import Config


async def add_access_point_name(
    client: ClientSession, data: AccessPointRequestNew, config: Config, **kwargs
) -> AccessPointReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessPointRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessPointReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-access-point-name"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessPointReply(**resp)
