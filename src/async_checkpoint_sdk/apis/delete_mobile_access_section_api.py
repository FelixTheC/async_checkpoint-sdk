from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.mobile_applications_section_identifier_request_show import (
    MobileApplicationsSectionIdentifierRequestShow,
)
from config import Config


async def delete_mobile_access_section(
    client: ClientSession,
    data: MobileApplicationsSectionIdentifierRequestShow,
    config: Config,
    **kwargs,
) -> ApiOkReply:
    """
    Delete existing Mobile Access section using section name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileApplicationsSectionIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-mobile-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
