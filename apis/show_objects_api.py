from aiohttp import ClientSession

from config import Config
from models.query_objects_reply import QueryObjectsReply
from models.query_objects_request import QueryObjectsRequest


async def show_objects(
    client: ClientSession, data: QueryObjectsRequest, config: Config, **kwargs
) -> QueryObjectsReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : QueryObjectsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    QueryObjectsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-objects"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return QueryObjectsReply(**resp)
