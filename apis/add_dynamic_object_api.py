from config import Config
from aiohttp import ClientSession
from models.dynamic_object_reply import DynamicObjectReply
from models.dynamic_object_request_new import DynamicObjectRequestNew


async def add_dynamic_object(
    client: ClientSession, data: DynamicObjectRequestNew, config: Config, **kwargs
) -> DynamicObjectReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DynamicObjectRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DynamicObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-dynamic-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicObjectReply(**resp)
