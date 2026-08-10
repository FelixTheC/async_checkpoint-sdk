from aiohttp import ClientSession

from async_checkpoint_sdk.models.file_data_type_reply import FileDataTypeReply
from async_checkpoint_sdk.models.file_data_type_request_new import FileDataTypeRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_data_type_file_attributes(
    client: ClientSession, data: FileDataTypeRequestNew, config: SDKConfig, **kwargs
) -> FileDataTypeReply:
    """
    Create new File Attributes Data Type Object.

    Parameters
    ----------
    client : ClientSession
    data : FileDataTypeRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    FileDataTypeReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-type-file-attributes"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return FileDataTypeReply(**resp)
