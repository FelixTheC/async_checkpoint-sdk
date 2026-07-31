from aiohttp import ClientSession

from async_checkpoint_sdk.models.show_ha_state_reply import ShowHaStateReply
from async_checkpoint_sdk.models.show_ha_state_request import ShowHaStateRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_ha_state(
    client: ClientSession, data: ShowHaStateRequest, config: SDKConfig, **kwargs
) -> ShowHaStateReply:
    """
    Retrieve domain high availability state.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowHaStateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ShowHaStateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ha-state"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowHaStateReply(**resp)
