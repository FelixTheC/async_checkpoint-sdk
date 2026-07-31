from aiohttp import ClientSession

from async_checkpoint_sdk.models.host_reply import HostReply
from async_checkpoint_sdk.models.host_request_new import HostRequestNew
from config import Config


async def add_host(
    client: ClientSession, data: HostRequestNew, config: Config, **kwargs
) -> HostReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : HostRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    HostReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-host"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return HostReply(**resp)
