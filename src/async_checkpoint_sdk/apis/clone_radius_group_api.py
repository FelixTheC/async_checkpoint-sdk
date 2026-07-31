from aiohttp import ClientSession

from async_checkpoint_sdk.models.radius_group_reply import RadiusGroupReply
from async_checkpoint_sdk.models.radius_group_request_edit import RadiusGroupRequestEdit
from config import Config


async def clone_radius_group(
    client: ClientSession, data: RadiusGroupRequestEdit, config: Config, **kwargs
) -> RadiusGroupReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : RadiusGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
