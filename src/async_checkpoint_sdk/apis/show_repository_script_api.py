from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.script_reply import ScriptReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_repository_script(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> ScriptReply:
    """
    Show a script in the script repository.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ScriptReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-repository-script"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScriptReply(**resp)
