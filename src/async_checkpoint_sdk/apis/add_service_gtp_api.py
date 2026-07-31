from aiohttp import ClientSession

from async_checkpoint_sdk.models.gtp_service_reply import GtpServiceReply
from async_checkpoint_sdk.models.gtp_service_request_new import GtpServiceRequestNew
from config import Config


async def add_service_gtp(
    client: ClientSession, data: GtpServiceRequestNew, config: Config, **kwargs
) -> GtpServiceReply:
    """
    Create a new GTP service object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GtpServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
