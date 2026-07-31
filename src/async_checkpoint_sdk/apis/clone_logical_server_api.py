from aiohttp import ClientSession

from async_checkpoint_sdk.models.logical_server_reply import LogicalServerReply
from async_checkpoint_sdk.models.logical_server_request_edit import LogicalServerRequestEdit
from config import Config


async def clone_logical_server(
    client: ClientSession, data: LogicalServerRequestEdit, config: Config, **kwargs
) -> LogicalServerReply:
    """
    Clone existing logical server.

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
    url = f"https://{config.server}:{config.port}/web_api/clone-logical-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LogicalServerReply(**resp)
