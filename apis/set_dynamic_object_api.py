from config import Config
from aiohttp import ClientSession
from models.dynamic_object_reply import DynamicObjectReply
from models.dynamic_object_request_edit import DynamicObjectRequestEdit


async def set_dynamic_object(
    client: ClientSession, data: DynamicObjectRequestEdit, config: Config, **kwargs
) -> DynamicObjectReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DynamicObjectRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DynamicObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-dynamic-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicObjectReply(**resp)
