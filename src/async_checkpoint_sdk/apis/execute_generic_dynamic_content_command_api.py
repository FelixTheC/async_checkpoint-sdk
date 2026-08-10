from aiohttp import ClientSession

from async_checkpoint_sdk.models.generic_dynamic_content_command_reply import (
    GenericDynamicContentCommandReply,
)
from async_checkpoint_sdk.models.generic_dynamic_content_command_request import (
    GenericDynamicContentCommandRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def execute_generic_dynamic_content_command(
    client: ClientSession, data: GenericDynamicContentCommandRequest, config: SDKConfig, **kwargs
) -> GenericDynamicContentCommandReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : GenericDynamicContentCommandRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    GenericDynamicContentCommandReply

    """
    url = f"https://{config.server}:{config.port}/web_api/execute-generic-dynamic-content-command"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GenericDynamicContentCommandReply(**resp)
