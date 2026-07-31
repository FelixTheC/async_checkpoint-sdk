from aiohttp import ClientSession

from config import Config
from models.gateway_global_use_reply import GatewayGlobalUseReply
from models.gateway_global_use_request_show import GatewayGlobalUseRequestShow


async def show_gateway_global_use(
    client: ClientSession, data: GatewayGlobalUseRequestShow, config: Config, **kwargs
) -> GatewayGlobalUseReply:
    """
    Show global usage of a specific target.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GatewayGlobalUseRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GatewayGlobalUseReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-gateway-global-use"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GatewayGlobalUseReply(**resp)
