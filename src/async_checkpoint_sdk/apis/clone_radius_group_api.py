from aiohttp import ClientSession

from async_checkpoint_sdk.models.radius_group_reply import RadiusGroupReply
from async_checkpoint_sdk.models.radius_group_request_edit import RadiusGroupRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_radius_group(
    client: ClientSession, data: RadiusGroupRequestEdit, config: SDKConfig, **kwargs
) -> RadiusGroupReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : RadiusGroupRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    RadiusGroupReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-radius-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RadiusGroupReply(**resp)
