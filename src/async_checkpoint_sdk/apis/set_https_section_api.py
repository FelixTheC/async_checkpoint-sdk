from aiohttp import ClientSession

from async_checkpoint_sdk.models.t_l_s_section_reply import TLSSectionReply
from async_checkpoint_sdk.models.t_l_s_section_request_edit import TLSSectionRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_https_section(
    client: ClientSession, data: TLSSectionRequestEdit, config: SDKConfig, **kwargs
) -> TLSSectionReply:
    """
    Edit existing HTTPS Inspection section using section name or uid and layer name.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TLSSectionRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TLSSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-https-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TLSSectionReply(**resp)
