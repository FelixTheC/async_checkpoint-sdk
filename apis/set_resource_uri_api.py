from config import Config
from aiohttp import ClientSession
from models.uri_resource_reply import UriResourceReply
from models.uri_resource_request_edit import UriResourceRequestEdit


async def set_resource_uri(
    client: ClientSession, data: UriResourceRequestEdit, config: Config, **kwargs
) -> UriResourceReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UriResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UriResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-resource-uri"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UriResourceReply(**resp)
