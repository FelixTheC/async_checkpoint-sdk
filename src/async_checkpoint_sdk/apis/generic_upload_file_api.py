from aiohttp import ClientSession

from async_checkpoint_sdk.models.generic_upload_file_reply import GenericUploadFileReply
from async_checkpoint_sdk.models.generic_upload_file_request import GenericUploadFileRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def generic_upload_file(
    client: ClientSession, data: GenericUploadFileRequest, config: SDKConfig, **kwargs
) -> GenericUploadFileReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : GenericUploadFileRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    GenericUploadFileReply

    """
    url = f"https://{config.server}:{config.port}/web_api/generic-upload-file"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GenericUploadFileReply(**resp)
