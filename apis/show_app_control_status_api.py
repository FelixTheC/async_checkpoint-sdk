from config import Config
from aiohttp import ClientSession
from models.appi_status_reply import AppiStatusReply
from models.appi_status_request import AppiStatusRequest


async def show_app_control_status(
    client: ClientSession, data: AppiStatusRequest, config: Config, **kwargs
) -> AppiStatusReply:
    """
    Retrieve existing Application Control and URL Filtering update status.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AppiStatusRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-app-control-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AppiStatusReply(**resp)
