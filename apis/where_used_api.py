from config import Config
from aiohttp import ClientSession
from models.where_used_object_reply import WhereUsedObjectReply
from models.where_used_object_request import WhereUsedObjectRequest


async def where_used(
    client: ClientSession, data: WhereUsedObjectRequest, config: Config, **kwargs
) -> WhereUsedObjectReply:
    """
    Searches for usage of the target object in other objects and rules.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WhereUsedObjectRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WhereUsedObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/where-used"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WhereUsedObjectReply(**resp)
