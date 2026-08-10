from aiohttp import ClientSession

from async_checkpoint_sdk.models.notification_subscribe_reply import NotificationSubscribeReply
from async_checkpoint_sdk.models.notification_subscribe_request import NotificationSubscribeRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def subscribe_notification(
    client: ClientSession, data: NotificationSubscribeRequest, config: SDKConfig, **kwargs
) -> NotificationSubscribeReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : NotificationSubscribeRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    NotificationSubscribeReply

    """
    url = f"https://{config.server}:{config.port}/web_api/subscribe-notification"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NotificationSubscribeReply(**resp)
