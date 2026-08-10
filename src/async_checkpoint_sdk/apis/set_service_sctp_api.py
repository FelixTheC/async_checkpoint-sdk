from aiohttp import ClientSession

from async_checkpoint_sdk.models.sctp_service_reply import SctpServiceReply
from async_checkpoint_sdk.models.sctp_service_request_edit import SctpServiceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_service_sctp(
    client: ClientSession, data: SctpServiceRequestEdit, config: SDKConfig, **kwargs
) -> SctpServiceReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : SctpServiceRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SctpServiceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-service-sctp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SctpServiceReply(**resp)
