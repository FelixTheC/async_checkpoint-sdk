from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.multiple_key_exchanges_reply import MultipleKeyExchangesReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_multiple_key_exchanges(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> MultipleKeyExchangesReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MultipleKeyExchangesReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-multiple-key-exchanges"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MultipleKeyExchangesReply(**resp)
