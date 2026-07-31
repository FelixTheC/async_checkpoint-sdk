from aiohttp import ClientSession

from config import Config
from models.set_active_reply import SetActiveReply
from models.set_active_request import SetActiveRequest


async def make_server_active(
    client: ClientSession, data: SetActiveRequest, config: Config, **kwargs
) -> SetActiveReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SetActiveRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SetActiveReply
    """
    url = f"https://{config.server}:{config.port}/web_api/make-server-active"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SetActiveReply(**resp)
