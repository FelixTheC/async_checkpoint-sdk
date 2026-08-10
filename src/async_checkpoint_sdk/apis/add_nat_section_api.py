from aiohttp import ClientSession

from async_checkpoint_sdk.models.nat_section_reply import NatSectionReply
from async_checkpoint_sdk.models.nat_section_request_new import NatSectionRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_nat_section(
    client: ClientSession, data: NatSectionRequestNew, config: SDKConfig, **kwargs
) -> NatSectionReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : NatSectionRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    NatSectionReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-nat-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NatSectionReply(**resp)
