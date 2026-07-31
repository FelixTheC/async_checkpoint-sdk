from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.lsm_gw_profile_reply import LsmGwProfileReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_lsm_gateway_profile(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> LsmGwProfileReply:
    """
    Show LSM Gateway Profile.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LsmGwProfileReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-lsm-gateway-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmGwProfileReply(**resp)
