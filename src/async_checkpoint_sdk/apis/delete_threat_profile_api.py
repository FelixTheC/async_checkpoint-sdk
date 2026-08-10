from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_delete import (
    ApiVisualCPObjectIdentifierRequestDelete,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_threat_profile(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestDelete, config: SDKConfig, **kwargs
) -> ApiTaskReply:
    """
    Delete existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestDelete
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiTaskReply

    """
    url = f"https://{config.server}:{config.port}/web_api/delete-threat-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
