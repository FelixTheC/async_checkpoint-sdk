from aiohttp import ClientSession

from async_checkpoint_sdk.models.weighted_words_reply import WeightedWordsReply
from async_checkpoint_sdk.models.weighted_words_request_new import WeightedWordsRequestNew
from config import Config


async def add_data_type_weighted_keywords(
    client: ClientSession, data: WeightedWordsRequestNew, config: Config, **kwargs
) -> WeightedWordsReply:
    """
    Create new Weighted Keywords Data Type Object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WeightedWordsRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WeightedWordsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-type-weighted-keywords"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WeightedWordsReply(**resp)
