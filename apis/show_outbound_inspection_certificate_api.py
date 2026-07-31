from aiohttp import ClientSession

from config import Config
from models.outbound_certificate_reply import OutboundCertificateReply
from models.outbound_certificate_request_show import OutboundCertificateRequestShow


async def show_outbound_inspection_certificate(
    client: ClientSession, data: OutboundCertificateRequestShow, config: Config, **kwargs
) -> OutboundCertificateReply:
    """
    Retrieve existing Outbound Certificate using object name or uid. If an Identifier wasn't given, the default Outbound Certificate is returned if it exists.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : OutboundCertificateRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OutboundCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-outbound-inspection-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OutboundCertificateReply(**resp)
