from aiohttp import ClientSession

from async_checkpoint_sdk.models.host_ckp_reply import HostCkpReply
from async_checkpoint_sdk.models.host_ckp_request_new import HostCkpRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_checkpoint_host(
    client: ClientSession, data: HostCkpRequestNew, config: SDKConfig, **kwargs
) -> HostCkpReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : HostCkpRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
