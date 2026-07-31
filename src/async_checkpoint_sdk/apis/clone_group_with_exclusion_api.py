from aiohttp import ClientSession

from async_checkpoint_sdk.models.group_with_exclusion_reply import GroupWithExclusionReply
from async_checkpoint_sdk.models.group_with_exclusion_request_edit import (
    GroupWithExclusionRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_group_with_exclusion(
    client: ClientSession, data: GroupWithExclusionRequestEdit, config: SDKConfig, **kwargs
) -> GroupWithExclusionReply:
    """
    Clone existing object.

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
    url = f"https://{config.server}:{config.port}/web_api/clone-group-with-exclusion"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GroupWithExclusionReply(**resp)
