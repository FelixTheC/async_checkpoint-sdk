from config import Config
from aiohttp import ClientSession
from models.key_words_data_type_reply import KeyWordsDataTypeReply
from models.key_words_data_type_request_new import KeyWordsDataTypeRequestNew


async def add_data_type_keywords(
    client: ClientSession, data: KeyWordsDataTypeRequestNew, config: Config, **kwargs
) -> KeyWordsDataTypeReply:
    """
    Create new Keywords Data Type Object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : KeyWordsDataTypeRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    KeyWordsDataTypeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-type-keywords"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return KeyWordsDataTypeReply(**resp)
