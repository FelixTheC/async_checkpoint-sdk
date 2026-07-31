from config import Config
from aiohttp import ClientSession
from models.api_task_reply import ApiTaskReply
from models.profile_request_edit import ProfileRequestEdit


async def set_threat_profile(
    client: ClientSession, data: ProfileRequestEdit, config: Config, **kwargs
) -> ApiTaskReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ProfileRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-threat-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
