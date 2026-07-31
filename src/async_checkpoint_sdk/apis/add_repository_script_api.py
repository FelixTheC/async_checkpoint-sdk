from aiohttp import ClientSession

from async_checkpoint_sdk.models.script_reply import ScriptReply
from async_checkpoint_sdk.models.script_request_new import ScriptRequestNew
from config import Config


async def add_repository_script(
    client: ClientSession, data: ScriptRequestNew, config: Config, **kwargs
) -> ScriptReply:
    """
    Add a new script to the script repository.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ScriptRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ScriptReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-repository-script"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScriptReply(**resp)
