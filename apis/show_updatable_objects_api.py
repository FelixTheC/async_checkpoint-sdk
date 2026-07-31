from config import Config
from aiohttp import ClientSession
from models.api_query_object_reply import ApiQueryObjectReply
from models.object_in_group_query_request import ObjectInGroupQueryRequest


async def show_updatable_objects(
    client: ClientSession, data: ObjectInGroupQueryRequest, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieves all Updatable Objects that were imported to the Management Server.
    
    Parameters
    ----------
    client : ClientSession [Argument]
        data : ObjectInGroupQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    data : ObjectInGroupQueryRequest [Argument]
        data : ObjectInGroupQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-updatable-objects"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
