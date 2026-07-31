from aiohttp import ClientSession

from async_checkpoint_sdk.models.client_login_option_reply import ClientLoginOptionReply
from async_checkpoint_sdk.models.client_login_option_request_edit import (
    ClientLoginOptionRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_client_login_option(
    client: ClientSession, data: ClientLoginOptionRequestEdit, config: SDKConfig, **kwargs
) -> ClientLoginOptionReply:
    """
    Clone existing client login option.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ClientLoginOptionRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClientLoginOptionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-client-login-option"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClientLoginOptionReply(**resp)
