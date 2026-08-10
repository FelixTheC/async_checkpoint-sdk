from aiohttp import ClientSession

from async_checkpoint_sdk.models.internal_trusted_ca_request_show import (
    InternalTrustedCaRequestShow,
)
from async_checkpoint_sdk.models.trusted_ca_reply import TrustedCaReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_internal_trusted_ca(
    client: ClientSession, data: InternalTrustedCaRequestShow, config: SDKConfig, **kwargs
) -> TrustedCaReply:
    """
    Retrieve existing Internal CA object.

    Parameters
    ----------
    client : ClientSession
    data : InternalTrustedCaRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TrustedCaReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-internal-trusted-ca"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaReply(**resp)
