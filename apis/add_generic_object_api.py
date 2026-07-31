from config import Config
from aiohttp import ClientSession
from models.generic_object_request_add import GenericObjectRequestAdd
from models.generic_object_api_reply import GenericObjectApiReply


async def add_generic_object(
    client: ClientSession, data: GenericObjectRequestAdd, config: Config, **kwargs
) -> GenericObjectApiReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GenericObjectRequestAdd [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GenericObjectApiReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-generic-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GenericObjectApiReply(**resp)
