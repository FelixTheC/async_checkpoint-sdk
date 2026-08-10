from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_section_reply import AccessSectionReply
from async_checkpoint_sdk.models.access_section_request_edit import AccessSectionRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_access_section(
    client: ClientSession, data: AccessSectionRequestEdit, config: SDKConfig, **kwargs
) -> AccessSectionReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : AccessSectionRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    AccessSectionReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessSectionReply(**resp)
