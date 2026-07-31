from aiohttp import ClientSession

from async_checkpoint_sdk.models.other_service_reply import OtherServiceReply
from async_checkpoint_sdk.models.other_service_request_edit import OtherServiceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_service_other(
    client: ClientSession, data: OtherServiceRequestEdit, config: SDKConfig, **kwargs
) -> OtherServiceReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : OtherServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OtherServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-service-other"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OtherServiceReply(**resp)
