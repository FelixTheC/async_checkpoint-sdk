from config import Config
from aiohttp import ClientSession
from models.generic_object_request_edit import GenericObjectRequestEdit
from models.dynamic_content_object_api_reply import DynamicContentObjectApiReply


async def set_dynamic_content(
    client: ClientSession, data: GenericObjectRequestEdit, config: Config, **kwargs
) -> DynamicContentObjectApiReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GenericObjectRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DynamicContentObjectApiReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-dynamic-content"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicContentObjectApiReply(**resp)
