from aiohttp import ClientSession

from async_checkpoint_sdk.models.web_api_server_status_reply import WebApiServerStatusReply
from async_checkpoint_sdk.models.web_api_server_status_request import WebApiServerStatusRequest
from config import Config


async def show_api_status(
    client: ClientSession, data: WebApiServerStatusRequest, config: Config, **kwargs
) -> WebApiServerStatusReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WebApiServerStatusRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WebApiServerStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-api-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebApiServerStatusReply(**resp)
