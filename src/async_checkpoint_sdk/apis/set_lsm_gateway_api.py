from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_gateway_reply import LsmGatewayReply
from async_checkpoint_sdk.models.lsm_gateway_request_edit import LsmGatewayRequestEdit
from config import Config


async def set_lsm_gateway(
    client: ClientSession, data: LsmGatewayRequestEdit, config: Config, **kwargs
) -> LsmGatewayReply:
    """
    Edit existing LSM Gateway.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LsmGatewayRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LsmGatewayReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-lsm-gateway"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmGatewayReply(**resp)
