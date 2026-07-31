from aiohttp import ClientSession

from async_checkpoint_sdk.models.outbound_certificate_reply import OutboundCertificateReply
from async_checkpoint_sdk.models.outbound_certificate_request_edit import (
    OutboundCertificateRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_outbound_inspection_certificate(
    client: ClientSession, data: OutboundCertificateRequestEdit, config: SDKConfig, **kwargs
) -> OutboundCertificateReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : OutboundCertificateRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OutboundCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-outbound-inspection-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OutboundCertificateReply(**resp)
