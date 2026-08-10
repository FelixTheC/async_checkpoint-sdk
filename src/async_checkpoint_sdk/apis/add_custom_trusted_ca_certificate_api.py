from aiohttp import ClientSession

from async_checkpoint_sdk.models.custom_trusted_ca_certificate_reply import (
    CustomTrustedCaCertificateReply,
)
from async_checkpoint_sdk.models.custom_trusted_ca_certificate_request_new import (
    CustomTrustedCaCertificateRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_custom_trusted_ca_certificate(
    client: ClientSession, data: CustomTrustedCaCertificateRequestNew, config: SDKConfig, **kwargs
) -> CustomTrustedCaCertificateReply:
    """
    Create new custom trusted CA certificate.

    Parameters
    ----------
    client : ClientSession
    data : CustomTrustedCaCertificateRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    CustomTrustedCaCertificateReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-custom-trusted-ca-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CustomTrustedCaCertificateReply(**resp)
