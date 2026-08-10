from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_base_command_reply import LsmBaseCommandReply
from async_checkpoint_sdk.models.lsm_run_script_request import LsmRunScriptRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def lsm_run_script(
    client: ClientSession, data: LsmRunScriptRequest, config: SDKConfig, **kwargs
) -> LsmBaseCommandReply:
    """
    Executes the lsm-run-script on a given list of targets. Run the given script on the targets devices.

    Parameters
    ----------
    client : ClientSession
    data : LsmRunScriptRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LsmBaseCommandReply

    """
    url = f"https://{config.server}:{config.port}/web_api/lsm-run-script"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmBaseCommandReply(**resp)
