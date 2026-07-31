from config import Config
from aiohttp import ClientSession
from models.afw_control_request import AfwControlRequest
from models.afw_control_status_reply import AfwControlStatusReply


async def afw_status(
    client: ClientSession, data: AfwControlRequest, config: Config, **kwargs
) -> AfwControlStatusReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AfwControlRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AfwControlStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/afw-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AfwControlStatusReply(**resp)
