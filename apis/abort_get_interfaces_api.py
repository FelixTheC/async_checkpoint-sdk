from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.get_interfaces_abort_request import GetInterfacesAbortRequest


async def abort_get_interfaces(
    client: ClientSession, data: GetInterfacesAbortRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
        Attempt to abort an on-going "get-interfaces" operation.
    This API might fail if the "get-interfaces" operation is in its final stage.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GetInterfacesAbortRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/abort-get-interfaces"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
