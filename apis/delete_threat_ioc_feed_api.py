from aiohttp import ClientSession

from config import Config
from models.api_task_reply import ApiTaskReply
from models.api_visual_c_p_object_identifier_request_delete import (
    ApiVisualCPObjectIdentifierRequestDelete,
)


async def delete_threat_ioc_feed(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestDelete, config: Config, **kwargs
) -> ApiTaskReply:
    """
    Delete a Threat IOC feed.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestDelete [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-threat-ioc-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
