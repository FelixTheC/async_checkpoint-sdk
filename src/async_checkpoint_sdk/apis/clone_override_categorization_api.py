from aiohttp import ClientSession

from async_checkpoint_sdk.models.override_categorization_reply import OverrideCategorizationReply
from async_checkpoint_sdk.models.override_categorization_request_edit import (
    OverrideCategorizationRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_override_categorization(
    client: ClientSession, data: OverrideCategorizationRequestEdit, config: SDKConfig, **kwargs
) -> OverrideCategorizationReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : OverrideCategorizationRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    OverrideCategorizationReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-override-categorization"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OverrideCategorizationReply(**resp)
