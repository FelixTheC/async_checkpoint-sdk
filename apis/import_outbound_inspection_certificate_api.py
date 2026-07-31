from config import Config
from aiohttp import ClientSession
from models.outbound_certificate_reply import OutboundCertificateReply
from models.import_outbound_certificate_request import ImportOutboundCertificateRequest


async def import_outbound_inspection_certificate(
    client: ClientSession, data: ImportOutboundCertificateRequest, config: Config, **kwargs
) -> OutboundCertificateReply:
    """
    Import Outbound Inspection certificate for HTTPS inspection.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ImportOutboundCertificateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OutboundCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/import-outbound-inspection-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OutboundCertificateReply(**resp)
