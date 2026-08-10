from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.traditional_group_reply import TraditionalGroupReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_data_type_traditional_group(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> TraditionalGroupReply:
    """
    Retrieve existing Traditional Group Data Type using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TraditionalGroupReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-data-type-traditional-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TraditionalGroupReply(**resp)
