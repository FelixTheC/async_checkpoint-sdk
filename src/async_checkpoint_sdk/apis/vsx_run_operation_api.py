from aiohttp import ClientSession

from async_checkpoint_sdk.models.vsx_run_operation_reply import VsxRunOperationReply
from async_checkpoint_sdk.models.vsx_run_operation_request import VsxRunOperationRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def vsx_run_operation(
    client: ClientSession, data: VsxRunOperationRequest, config: SDKConfig, **kwargs
) -> VsxRunOperationReply:
    """
    Run the VSX operation by its name and parameters. <br><b>Important note:</b> An automatic session publish is part of all the operations in this API.

    Parameters
    ----------
    client : ClientSession
    data : VsxRunOperationRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    VsxRunOperationReply

    """
    url = f"https://{config.server}:{config.port}/web_api/vsx-run-operation"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VsxRunOperationReply(**resp)
