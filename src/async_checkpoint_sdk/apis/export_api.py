from aiohttp import ClientSession

from async_checkpoint_sdk.models.web_api_export_reply import WebApiExportReply
from async_checkpoint_sdk.models.web_api_export_request import WebApiExportRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def export(
    client: ClientSession, data: WebApiExportRequest, config: SDKConfig, **kwargs
) -> WebApiExportReply:
    """
    Export the Database.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WebApiExportRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WebApiExportReply
    """
    url = f"https://{config.server}:{config.port}/web_api/export"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebApiExportReply(**resp)
