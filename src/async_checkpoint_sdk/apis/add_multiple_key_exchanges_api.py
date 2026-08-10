from aiohttp import ClientSession

from async_checkpoint_sdk.models.multiple_key_exchanges_reply import MultipleKeyExchangesReply
from async_checkpoint_sdk.models.multiple_key_exchanges_request_new import (
    MultipleKeyExchangesRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_multiple_key_exchanges(
    client: ClientSession, data: MultipleKeyExchangesRequestNew, config: SDKConfig, **kwargs
) -> MultipleKeyExchangesReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : MultipleKeyExchangesRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MultipleKeyExchangesReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-multiple-key-exchanges"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MultipleKeyExchangesReply(**resp)
