from config import Config
from aiohttp import ClientSession
from models.sctp_service_reply import SctpServiceReply
from models.sctp_service_request_edit import SctpServiceRequestEdit


async def clone_service_sctp(
    client: ClientSession, data: SctpServiceRequestEdit, config: Config, **kwargs
) -> SctpServiceReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SctpServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SctpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-service-sctp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SctpServiceReply(**resp)
