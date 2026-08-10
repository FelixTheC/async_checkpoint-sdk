from aiohttp import ClientSession

from async_checkpoint_sdk.models.mds_reply import MdsReply
from async_checkpoint_sdk.models.mds_request_edit import MdsRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_mds(
    client: ClientSession, data: MdsRequestEdit, config: SDKConfig, **kwargs
) -> MdsReply:
    """
    Edit existing object of type Multi-Domain Server or Multi-Domain Log Server using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : MdsRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MdsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-mds"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdsReply(**resp)
