from aiohttp import ClientSession

from async_checkpoint_sdk.models.override_categorization_reply import OverrideCategorizationReply
from async_checkpoint_sdk.models.override_categorization_request_show import (
    OverrideCategorizationRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_override_categorization(
    client: ClientSession, data: OverrideCategorizationRequestShow, config: SDKConfig, **kwargs
) -> OverrideCategorizationReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : OverrideCategorizationRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    OverrideCategorizationReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-override-categorization"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OverrideCategorizationReply(**resp)
