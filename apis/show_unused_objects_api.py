from aiohttp import ClientSession

from config import Config
from models.api_query_object_reply import ApiQueryObjectReply
from models.object_in_group_with_members_query_request import ObjectInGroupWithMembersQueryRequest


async def show_unused_objects(
    client: ClientSession, data: ObjectInGroupWithMembersQueryRequest, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all unused objects.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ObjectInGroupWithMembersQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-unused-objects"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
