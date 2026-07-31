from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.delete_api_key_request import DeleteApiKeyRequest


async def delete_api_key(
    client: ClientSession, data: DeleteApiKeyRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete the API key. For the key to be invalid publish is needed.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DeleteApiKeyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-api-key"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
