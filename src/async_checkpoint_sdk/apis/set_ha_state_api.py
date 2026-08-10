from aiohttp import ClientSession

from async_checkpoint_sdk.models.set_ha_state_reply import SetHaStateReply
from async_checkpoint_sdk.models.set_ha_state_request import SetHaStateRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_ha_state(
    client: ClientSession, data: SetHaStateRequest, config: SDKConfig, **kwargs
) -> SetHaStateReply:
    """
    Switch domain server high availability state. </br>After switching domain server to standby state, the session expires and you need to login again. <br/>You can run this command from a user or global domain on Multi Domain Server and from the user domain on Security Management Server.

    Parameters
    ----------
    client : ClientSession
    data : SetHaStateRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
