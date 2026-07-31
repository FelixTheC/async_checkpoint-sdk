from config import Config
from aiohttp import ClientSession
from models.tacacs_reply import TacacsReply
from models.tacacs_request_edit import TacacsRequestEdit


async def clone_tacacs_server(
    client: ClientSession, data: TacacsRequestEdit, config: Config, **kwargs
) -> TacacsReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TacacsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TacacsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-tacacs-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TacacsReply(**resp)
