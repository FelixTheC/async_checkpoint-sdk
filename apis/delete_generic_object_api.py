from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.generic_object_identifier_request import GenericObjectIdentifierRequest


async def delete_generic_object(
    client: ClientSession, data: GenericObjectIdentifierRequest, config: Config, **kwargs
) -> ApiOkReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GenericObjectIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-generic-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
