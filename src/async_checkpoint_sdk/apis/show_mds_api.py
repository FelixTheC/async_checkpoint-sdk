from aiohttp import ClientSession

from async_checkpoint_sdk.models.mds_reply import MdsReply
from async_checkpoint_sdk.models.mds_request_show import MdsRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_mds(
    client: ClientSession, data: MdsRequestShow, config: SDKConfig, **kwargs
) -> MdsReply:
    """
    Retrieve existing object of type Multi-Domain Server or Multi-Domain Log Server using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MdsRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MdsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-mds"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdsReply(**resp)
