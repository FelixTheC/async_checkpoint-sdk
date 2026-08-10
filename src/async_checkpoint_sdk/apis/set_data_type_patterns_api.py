from aiohttp import ClientSession

from async_checkpoint_sdk.models.patterns_data_type_reply import PatternsDataTypeReply
from async_checkpoint_sdk.models.patterns_data_type_request_edit import PatternsDataTypeRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_data_type_patterns(
    client: ClientSession, data: PatternsDataTypeRequestEdit, config: SDKConfig, **kwargs
) -> PatternsDataTypeReply:
    """
    Edit existing Pattern Data Type object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : PatternsDataTypeRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    PatternsDataTypeReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-type-patterns"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PatternsDataTypeReply(**resp)
