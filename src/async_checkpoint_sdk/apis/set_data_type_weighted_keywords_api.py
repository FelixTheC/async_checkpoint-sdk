from aiohttp import ClientSession

from async_checkpoint_sdk.models.weighted_words_reply import WeightedWordsReply
from async_checkpoint_sdk.models.weighted_words_request_edit import WeightedWordsRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_data_type_weighted_keywords(
    client: ClientSession, data: WeightedWordsRequestEdit, config: SDKConfig, **kwargs
) -> WeightedWordsReply:
    """
    Edit existing Weighted Keywords Data Type object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WeightedWordsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WeightedWordsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-type-weighted-keywords"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WeightedWordsReply(**resp)
