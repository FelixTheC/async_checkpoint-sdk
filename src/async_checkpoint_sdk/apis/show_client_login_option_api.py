from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.client_login_option_reply import ClientLoginOptionReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_client_login_option(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> ClientLoginOptionReply:
    """
    Retrieve existing client login option configuration using name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClientLoginOptionReply
    config : Config [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClientLoginOptionReply
    config : Config [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClientLoginOptionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-client-login-option"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClientLoginOptionReply(**resp)
