from aiohttp import ClientSession

from config import Config
from models.generic_object_api_reply import GenericObjectApiReply
from models.generic_object_identifier_request import GenericObjectIdentifierRequest


async def show_generic_object(
    client: ClientSession, data: GenericObjectIdentifierRequest, config: Config, **kwargs
) -> GenericObjectApiReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GenericObjectIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GenericObjectApiReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-generic-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GenericObjectApiReply(**resp)
