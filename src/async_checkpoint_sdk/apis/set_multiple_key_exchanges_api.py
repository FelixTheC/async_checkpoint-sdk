from aiohttp import ClientSession

from async_checkpoint_sdk.models.multiple_key_exchanges_reply import MultipleKeyExchangesReply
from async_checkpoint_sdk.models.multiple_key_exchanges_request_edit import (
    MultipleKeyExchangesRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_multiple_key_exchanges(
    client: ClientSession, data: MultipleKeyExchangesRequestEdit, config: SDKConfig, **kwargs
) -> MultipleKeyExchangesReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : MultipleKeyExchangesRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MultipleKeyExchangesReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-multiple-key-exchanges"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MultipleKeyExchangesReply(**resp)
