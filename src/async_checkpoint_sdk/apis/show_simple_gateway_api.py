from aiohttp import ClientSession

from async_checkpoint_sdk.models.gateway_ckp_reply import GatewayCkpReply
from async_checkpoint_sdk.models.gateway_ckp_request_show import GatewayCkpRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_simple_gateway(
    client: ClientSession, data: GatewayCkpRequestShow, config: SDKConfig, **kwargs
) -> GatewayCkpReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GatewayCkpRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GatewayCkpReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-simple-gateway"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GatewayCkpReply(**resp)
