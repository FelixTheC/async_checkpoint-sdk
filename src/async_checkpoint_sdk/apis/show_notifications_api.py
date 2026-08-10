from aiohttp import ClientSession

from async_checkpoint_sdk.models.notification_query_reply import NotificationQueryReply
from async_checkpoint_sdk.models.notification_query_request import NotificationQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_notifications(
    client: ClientSession, data: NotificationQueryRequest, config: SDKConfig, **kwargs
) -> NotificationQueryReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : NotificationQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    NotificationQueryReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-notifications"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NotificationQueryReply(**resp)
