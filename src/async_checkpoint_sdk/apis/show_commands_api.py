from aiohttp import ClientSession

from async_checkpoint_sdk.models.show_commands_reply import ShowCommandsReply
from async_checkpoint_sdk.models.show_commands_request import ShowCommandsRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_commands(
    client: ClientSession, data: ShowCommandsRequest, config: SDKConfig, **kwargs
) -> ShowCommandsReply:
    """
    Retrieve all of the supported Management API commands with their description.

    Parameters
    ----------
    client : ClientSession
    data : ShowCommandsRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ShowCommandsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-commands"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowCommandsReply(**resp)
