from config import Config
from aiohttp import ClientSession
from models.show_ha_status_reply import ShowHaStatusReply
from models.show_ha_status_request import ShowHaStatusRequest


async def show_ha_status(
    client: ClientSession, data: ShowHaStatusRequest, config: Config, **kwargs
) -> ShowHaStatusReply:
    """
    Retrieve domain high availability status.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowHaStatusRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ShowHaStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ha-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowHaStatusReply(**resp)
