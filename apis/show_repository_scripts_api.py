from config import Config
from aiohttp import ClientSession
from models.api_query_object_reply import ApiQueryObjectReply
from models.script_query import ScriptQuery


async def show_repository_scripts(
    client: ClientSession, data: ScriptQuery, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all objects.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ScriptQuery [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-repository-scripts"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
