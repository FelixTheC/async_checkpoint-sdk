from aiohttp import ClientSession

from config import Config
from models.set_ha_state_reply import SetHaStateReply
from models.set_ha_state_request import SetHaStateRequest


async def set_ha_state(
    client: ClientSession, data: SetHaStateRequest, config: Config, **kwargs
) -> SetHaStateReply:
    """
    Switch domain server high availability state. </br>After switching domain server to standby state, the session expires and you need to login again. <br/>You can run this command from a user or global domain on Multi Domain Server and from the user domain on Security Management Server.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SetHaStateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SetHaStateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-ha-state"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SetHaStateReply(**resp)
