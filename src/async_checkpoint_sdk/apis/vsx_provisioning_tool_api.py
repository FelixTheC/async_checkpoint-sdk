from aiohttp import ClientSession

from async_checkpoint_sdk.models.vpt_run_operation_reply import VptRunOperationReply
from async_checkpoint_sdk.models.vpt_run_operation_request import VptRunOperationRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def vsx_provisioning_tool(
    client: ClientSession, data: VptRunOperationRequest, config: SDKConfig, **kwargs
) -> VptRunOperationReply:
    """
    Run the VSX provisioning tool with the specified parameters. <br><b>Important note:</b> An automatic session publish is part of all the operations in this API.

    Parameters
    ----------
    client : ClientSession
    data : VptRunOperationRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
