from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.custom_trusted_ca_certificate_reply import (
    CustomTrustedCaCertificateReply,
)
from config import Config


async def show_custom_trusted_ca_certificate(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> CustomTrustedCaCertificateReply:
    """
    Retrieve existing custom trusted CA certificate using name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CustomTrustedCaCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-custom-trusted-ca-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CustomTrustedCaCertificateReply(**resp)
