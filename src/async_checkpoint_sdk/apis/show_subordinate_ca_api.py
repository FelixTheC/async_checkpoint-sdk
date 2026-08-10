from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.subordinate_ca_reply import SubordinateCaReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_subordinate_ca(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> SubordinateCaReply:
    """
    Retrieve existing Subordinate CA server using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SubordinateCaReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-subordinate-ca"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SubordinateCaReply(**resp)
