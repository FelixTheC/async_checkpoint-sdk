from aiohttp import ClientSession

from async_checkpoint_sdk.models.ck_reply import CkReply
from async_checkpoint_sdk.models.empty_request import EmptyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_ck(client: ClientSession, data: EmptyRequest, config: SDKConfig, **kwargs) -> CkReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ck"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CkReply(**resp)
