from config import Config
from aiohttp import ClientSession
from models.vpt_run_operation_request import VptRunOperationRequest
from models.vpt_run_operation_reply import VptRunOperationReply


async def vsx_provisioning_tool(
    client: ClientSession, data: VptRunOperationRequest, config: Config, **kwargs
) -> VptRunOperationReply:
    """
    Run the VSX provisioning tool with the specified parameters. <br><b>Important note:</b> An automatic session publish is part of all the operations in this API.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VptRunOperationRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VptRunOperationReply
    """
    url = f"https://{config.server}:{config.port}/web_api/vsx-provisioning-tool"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VptRunOperationReply(**resp)
