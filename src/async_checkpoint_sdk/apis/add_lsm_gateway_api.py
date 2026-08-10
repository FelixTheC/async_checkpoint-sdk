from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_gateway_reply import LsmGatewayReply
from async_checkpoint_sdk.models.lsm_gateway_request_new import LsmGatewayRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_lsm_gateway(
    client: ClientSession, data: LsmGatewayRequestNew, config: SDKConfig, **kwargs
) -> LsmGatewayReply:
    """
    Add LSM Gateway.

    Parameters
    ----------
    client : ClientSession
    data : LsmGatewayRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LsmGatewayReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-lsm-gateway"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmGatewayReply(**resp)
