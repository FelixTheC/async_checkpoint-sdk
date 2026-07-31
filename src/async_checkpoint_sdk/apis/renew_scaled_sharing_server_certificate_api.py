from aiohttp import ClientSession

from async_checkpoint_sdk.models.renew_scaled_sharing_certificate_reply import (
    RenewScaledSharingCertificateReply,
)
from async_checkpoint_sdk.models.renew_scaled_sharing_certificate_request import (
    RenewScaledSharingCertificateRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def renew_scaled_sharing_server_certificate(
    client: ClientSession, data: RenewScaledSharingCertificateRequest, config: SDKConfig, **kwargs
) -> RenewScaledSharingCertificateReply:
    """
    Renew the server certificate for the scaled sharing on the specified PDP Security Gateway or Cluster. <br>This operation generates a new certificate and replaces the existing certificate for scaled sharing. <br>Note - You must install the Access Control policy to apply the changes.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : RenewScaledSharingCertificateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    RenewScaledSharingCertificateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/renew-scaled-sharing-server-certificate"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RenewScaledSharingCertificateReply(**resp)
