from config import Config
from aiohttp import ClientSession
from models.run_script_request import RunScriptRequest
from models.cdm_command_reply import CdmCommandReply


async def run_script(
    client: ClientSession, data: RunScriptRequest, config: Config, **kwargs
) -> CdmCommandReply:
    """
    Executes the script on a given list of targets.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : RunScriptRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CdmCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-script"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CdmCommandReply(**resp)
