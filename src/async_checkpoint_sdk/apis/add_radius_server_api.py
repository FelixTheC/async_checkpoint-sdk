from aiohttp import ClientSession

from async_checkpoint_sdk.models.radius_reply import RadiusReply
from async_checkpoint_sdk.models.radius_request_new import RadiusRequestNew
from config import Config


async def add_radius_server(
    client: ClientSession, data: RadiusRequestNew, config: Config, **kwargs
) -> RadiusReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : RadiusRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    RadiusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-radius-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RadiusReply(**resp)
