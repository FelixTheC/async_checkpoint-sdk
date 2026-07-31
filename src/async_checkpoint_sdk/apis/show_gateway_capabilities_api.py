from aiohttp import ClientSession

from async_checkpoint_sdk.models.gateway_capabilities_reply import GatewayCapabilitiesReply
from async_checkpoint_sdk.models.gateway_capabilities_request import GatewayCapabilitiesRequest
from config import Config


async def show_gateway_capabilities(
    client: ClientSession, data: GatewayCapabilitiesRequest, config: Config, **kwargs
) -> GatewayCapabilitiesReply:
    """
    Show supported Check Point Gateway capabilities such as versions, hardware, platforms and blades.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GatewayCapabilitiesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GatewayCapabilitiesReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-gateway-capabilities"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GatewayCapabilitiesReply(**resp)
