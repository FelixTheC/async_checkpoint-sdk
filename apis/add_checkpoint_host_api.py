from config import Config
from aiohttp import ClientSession
from models.host_ckp_request_new import HostCkpRequestNew
from models.host_ckp_reply import HostCkpReply


async def add_checkpoint_host(
    client: ClientSession, data: HostCkpRequestNew, config: Config, **kwargs
) -> HostCkpReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : HostCkpRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    HostCkpReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-checkpoint-host"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return HostCkpReply(**resp)
