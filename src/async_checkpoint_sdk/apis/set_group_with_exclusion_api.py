from aiohttp import ClientSession

from async_checkpoint_sdk.models.group_with_exclusion_reply import GroupWithExclusionReply
from async_checkpoint_sdk.models.group_with_exclusion_request_edit import (
    GroupWithExclusionRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_group_with_exclusion(
    client: ClientSession, data: GroupWithExclusionRequestEdit, config: SDKConfig, **kwargs
) -> GroupWithExclusionReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GroupWithExclusionRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GroupWithExclusionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-group-with-exclusion"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GroupWithExclusionReply(**resp)
