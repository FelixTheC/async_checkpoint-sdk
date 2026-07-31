from aiohttp import ClientSession

from async_checkpoint_sdk.models.server_certificate_reply import ServerCertificateReply
from async_checkpoint_sdk.models.server_certificate_request_new import ServerCertificateRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_server_certificate(
    client: ClientSession, data: ServerCertificateRequestNew, config: SDKConfig, **kwargs
) -> ServerCertificateReply:
    """
    Import server certificates for inbound HTTPS traffic inspection.<br/> You can use the imported server certificates in the Certificate column of the HTTPS Inspection Policy.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServerCertificateRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServerCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-server-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServerCertificateReply(**resp)
