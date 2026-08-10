from aiohttp import ClientSession

from async_checkpoint_sdk.models.mds_reply import MdsReply
from async_checkpoint_sdk.models.mds_request_new import MdsRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_mds(client: ClientSession, data: MdsRequestNew, config: SDKConfig, **kwargs) -> MdsReply:
    """
    Create new object of type Multi-Domain Server or Multi-Domain Log Server.

    Parameters
    ----------
    client : ClientSession
    data : MdsRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MdsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-mds"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdsReply(**resp)
