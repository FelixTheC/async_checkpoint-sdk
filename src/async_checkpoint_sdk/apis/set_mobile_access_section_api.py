from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_applications_section_reply import (
    MobileApplicationsSectionReply,
)
from async_checkpoint_sdk.models.mobile_applications_section_request_edit import (
    MobileApplicationsSectionRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_mobile_access_section(
    client: ClientSession, data: MobileApplicationsSectionRequestEdit, config: SDKConfig, **kwargs
) -> MobileApplicationsSectionReply:
    """
    Edit existing Mobile Access section using section name or uid.

    Parameters
    ----------
    client : ClientSession
    data : MobileApplicationsSectionRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MobileApplicationsSectionReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-mobile-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileApplicationsSectionReply(**resp)
