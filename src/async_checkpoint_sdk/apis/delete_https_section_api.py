from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.t_l_s_section_identifier_request import (
    TLSSectionIdentifierRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_https_section(
    client: ClientSession, data: TLSSectionIdentifierRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Delete existing HTTPS Inspection section using section name or uid and layer name.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TLSSectionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-https-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
