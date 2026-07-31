from config import Config
from aiohttp import ClientSession
from models.radius_reply import RadiusReply
from models.radius_request_edit import RadiusRequestEdit


async def clone_radius_server(
    client: ClientSession, data: RadiusRequestEdit, config: Config, **kwargs
) -> RadiusReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : RadiusRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    RadiusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-radius-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RadiusReply(**resp)
