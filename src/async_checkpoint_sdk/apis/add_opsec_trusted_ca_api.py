from aiohttp import ClientSession

from async_checkpoint_sdk.models.opsec_trusted_ca_reply import OpsecTrustedCaReply
from async_checkpoint_sdk.models.opsec_trusted_ca_request_new import OpsecTrustedCaRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_opsec_trusted_ca(
    client: ClientSession, data: OpsecTrustedCaRequestNew, config: SDKConfig, **kwargs
) -> OpsecTrustedCaReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : OpsecTrustedCaRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    OpsecTrustedCaReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-opsec-trusted-ca"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OpsecTrustedCaReply(**resp)
