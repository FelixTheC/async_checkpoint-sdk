from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.trusted_ca_certificate_reply import TrustedCaCertificateReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_cp_trusted_ca_certificate(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> TrustedCaCertificateReply:
    """
    Retrieve existing Check Point trusted CA certificate using name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustedCaCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-cp-trusted-ca-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaCertificateReply(**resp)
