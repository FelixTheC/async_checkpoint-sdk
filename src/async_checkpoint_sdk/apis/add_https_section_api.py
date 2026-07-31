from aiohttp import ClientSession

from async_checkpoint_sdk.models.t_l_s_section_reply import TLSSectionReply
from async_checkpoint_sdk.models.t_l_s_section_request_new import TLSSectionRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_https_section(
    client: ClientSession, data: TLSSectionRequestNew, config: SDKConfig, **kwargs
) -> TLSSectionReply:
    """
    Create new HTTPS Inspection section.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TLSSectionRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TLSSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-https-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TLSSectionReply(**resp)
