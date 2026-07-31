from aiohttp import ClientSession

from async_checkpoint_sdk.models.logical_server_reply import LogicalServerReply
from async_checkpoint_sdk.models.logical_server_request_new import LogicalServerRequestNew
from config import Config


async def add_logical_server(
    client: ClientSession, data: LogicalServerRequestNew, config: Config, **kwargs
) -> LogicalServerReply:
    """
    Create new logical server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LogicalServerRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogicalServerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-logical-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LogicalServerReply(**resp)
