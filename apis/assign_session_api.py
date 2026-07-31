from aiohttp import ClientSession

from config import Config
from models.api_ok_reply import ApiOkReply
from models.work_session_assign_request import WorkSessionAssignRequest


async def assign_session(
    client: ClientSession, data: WorkSessionAssignRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Assign a session ownership to another administrator.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkSessionAssignRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/assign-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
