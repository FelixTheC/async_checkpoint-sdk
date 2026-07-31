from config import Config
from aiohttp import ClientSession
from models.radius_group_request_new import RadiusGroupRequestNew
from models.radius_group_reply import RadiusGroupReply


async def add_radius_group(
    client: ClientSession, data: RadiusGroupRequestNew, config: Config, **kwargs
) -> RadiusGroupReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : RadiusGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    RadiusGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-radius-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RadiusGroupReply(**resp)
