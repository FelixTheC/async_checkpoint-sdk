from aiohttp import ClientSession

from async_checkpoint_sdk.models.gtp_service_reply import GtpServiceReply
from async_checkpoint_sdk.models.gtp_service_request_new import GtpServiceRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_service_gtp(
    client: ClientSession, data: GtpServiceRequestNew, config: SDKConfig, **kwargs
) -> GtpServiceReply:
    """
    Create a new GTP service object.

    Parameters
    ----------
    client : ClientSession
    data : GtpServiceRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    GtpServiceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-gtp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GtpServiceReply(**resp)
