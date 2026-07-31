from aiohttp import ClientSession

from async_checkpoint_sdk.models.show_notification_subscriptions_reply import (
    ShowNotificationSubscriptionsReply,
)
from async_checkpoint_sdk.models.show_notification_subscriptions_request import (
    ShowNotificationSubscriptionsRequest,
)
from config import Config


async def show_subscriptions_notification(
    client: ClientSession, data: ShowNotificationSubscriptionsRequest, config: Config, **kwargs
) -> ShowNotificationSubscriptionsReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowNotificationSubscriptionsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ShowNotificationSubscriptionsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-subscriptions-notification"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowNotificationSubscriptionsReply(**resp)
