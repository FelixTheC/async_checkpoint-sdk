from aiohttp import ClientSession

from async_checkpoint_sdk.models.gtp_service_reply import GtpServiceReply
from async_checkpoint_sdk.models.gtp_service_request_edit import GtpServiceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_service_gtp(
    client: ClientSession, data: GtpServiceRequestEdit, config: SDKConfig, **kwargs
) -> GtpServiceReply:
    """
    Edit existing GTP service object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GtpServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GtpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-service-gtp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GtpServiceReply(**resp)
