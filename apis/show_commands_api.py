from config import Config
from aiohttp import ClientSession
from models.show_commands_reply import ShowCommandsReply
from models.show_commands_request import ShowCommandsRequest


async def show_commands(
    client: ClientSession, data: ShowCommandsRequest, config: Config, **kwargs
) -> ShowCommandsReply:
    """
    Retrieve all of the supported Management API commands with their description.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowCommandsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
