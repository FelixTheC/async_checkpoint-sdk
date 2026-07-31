from config import Config
from aiohttp import ClientSession
from models.server_certificate_reply import ServerCertificateReply
from models.server_certificate_request_edit import ServerCertificateRequestEdit


async def set_server_certificate(
    client: ClientSession, data: ServerCertificateRequestEdit, config: Config, **kwargs
) -> ServerCertificateReply:
    """
    Edit existing server certificate using name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServerCertificateRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServerCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-server-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServerCertificateReply(**resp)
