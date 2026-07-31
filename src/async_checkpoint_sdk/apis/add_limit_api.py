from aiohttp import ClientSession

from async_checkpoint_sdk.models.limit_reply import LimitReply
from async_checkpoint_sdk.models.limit_request_new import LimitRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_limit(
    client: ClientSession, data: LimitRequestNew, config: SDKConfig, **kwargs
) -> LimitReply:
    """
    Create new Limit object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LimitRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LimitReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-limit"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LimitReply(**resp)
