from aiohttp import ClientSession

from async_checkpoint_sdk.models.generic_object_query_reply import GenericObjectQueryReply
from async_checkpoint_sdk.models.generic_object_query_request import GenericObjectQueryRequest
from config import Config


async def show_generic_objects(
    client: ClientSession, data: GenericObjectQueryRequest, config: Config, **kwargs
) -> GenericObjectQueryReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GenericObjectQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GenericObjectQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-generic-objects"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GenericObjectQueryReply(**resp)
