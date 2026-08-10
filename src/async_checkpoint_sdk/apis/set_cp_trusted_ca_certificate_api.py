from aiohttp import ClientSession

from async_checkpoint_sdk.models.trusted_ca_certificate_reply import TrustedCaCertificateReply
from async_checkpoint_sdk.models.trusted_ca_certificate_request_edit import (
    TrustedCaCertificateRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_cp_trusted_ca_certificate(
    client: ClientSession, data: TrustedCaCertificateRequestEdit, config: SDKConfig, **kwargs
) -> TrustedCaCertificateReply:
    """
    Edit existing Check Point trusted CA certificate using name or uid. </br>By default all CP trusted CA certificates are enabled.

    Parameters
    ----------
    client : ClientSession
    data : TrustedCaCertificateRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TrustedCaCertificateReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-cp-trusted-ca-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaCertificateReply(**resp)
