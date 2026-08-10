from aiohttp import ClientSession

from async_checkpoint_sdk.models.script_reply import ScriptReply
from async_checkpoint_sdk.models.script_request_edit import ScriptRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_repository_script(
    client: ClientSession, data: ScriptRequestEdit, config: SDKConfig, **kwargs
) -> ScriptReply:
    """
    Edit an existing script in the script repository.

    Parameters
    ----------
    client : ClientSession
    data : ScriptRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ScriptReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-repository-script"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScriptReply(**resp)
