from config import Config
from aiohttp import ClientSession
from models.api_query_request import ApiQueryRequest
from models.api_query_object_reply import ApiQueryObjectReply


async def show_infinity_idp_objects(
    client: ClientSession, data: ApiQueryRequest, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all users/groups/machines from the Identity Provider.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-infinity-idp-objects"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
