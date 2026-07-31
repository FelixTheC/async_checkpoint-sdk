from config import Config
from aiohttp import ClientSession
from models.empty_request import EmptyRequest
from models.proxy_reply import ProxyReply


async def show_proxy(
    client: ClientSession, data: EmptyRequest, config: Config, **kwargs
) -> ProxyReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ProxyReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-proxy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ProxyReply(**resp)
