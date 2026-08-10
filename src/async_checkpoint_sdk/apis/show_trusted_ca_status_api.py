from aiohttp import ClientSession

from async_checkpoint_sdk.models.trusted_ca_status_reply import TrustedCaStatusReply
from async_checkpoint_sdk.models.trusted_ca_status_request import TrustedCaStatusRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_trusted_ca_status(
    client: ClientSession, data: TrustedCaStatusRequest, config: SDKConfig, **kwargs
) -> TrustedCaStatusReply:
    """
    Show Trusted CAs package status.

    Parameters
    ----------
    client : ClientSession
    data : TrustedCaStatusRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TrustedCaStatusReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-trusted-ca-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaStatusReply(**resp)
