from config import Config
from aiohttp import ClientSession
from models.logical_server_request_edit import LogicalServerRequestEdit
from models.logical_server_reply import LogicalServerReply


async def set_logical_server(
    client: ClientSession, data: LogicalServerRequestEdit, config: Config, **kwargs
) -> LogicalServerReply:
    """
    Edit existing logical server using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : LogicalServerRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogicalServerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-logical-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LogicalServerReply(**resp)
