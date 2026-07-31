from aiohttp import ClientSession

from async_checkpoint_sdk.models.key_words_data_type_reply import KeyWordsDataTypeReply
from async_checkpoint_sdk.models.key_words_data_type_request_edit import (
    KeyWordsDataTypeRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_data_type_keywords(
    client: ClientSession, data: KeyWordsDataTypeRequestEdit, config: SDKConfig, **kwargs
) -> KeyWordsDataTypeReply:
    """
    Edit existing Keywords Data Type object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : KeyWordsDataTypeRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    KeyWordsDataTypeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-type-keywords"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return KeyWordsDataTypeReply(**resp)
