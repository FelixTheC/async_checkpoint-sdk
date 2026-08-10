from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.server_certificate_reply import ServerCertificateReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_server_certificate(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> ServerCertificateReply:
    """
    Show existing server certificate using name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ServerCertificateReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-server-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServerCertificateReply(**resp)
