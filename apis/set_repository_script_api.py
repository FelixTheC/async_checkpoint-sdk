from config import Config
from aiohttp import ClientSession
from models.script_reply import ScriptReply
from models.script_request_edit import ScriptRequestEdit


async def set_repository_script(
    client: ClientSession, data: ScriptRequestEdit, config: Config, **kwargs
) -> ScriptReply:
    """
    Edit an existing script in the script repository.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ScriptRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
