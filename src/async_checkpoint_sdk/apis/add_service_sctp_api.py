from aiohttp import ClientSession

from async_checkpoint_sdk.models.sctp_service_reply import SctpServiceReply
from async_checkpoint_sdk.models.sctp_service_request_new import SctpServiceRequestNew
from config import Config


async def add_service_sctp(
    client: ClientSession, data: SctpServiceRequestNew, config: Config, **kwargs
) -> SctpServiceReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SctpServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SctpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-sctp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SctpServiceReply(**resp)
