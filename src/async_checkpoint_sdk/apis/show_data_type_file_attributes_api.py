from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.file_data_type_reply import FileDataTypeReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_data_type_file_attributes(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> FileDataTypeReply:
    """
    Retrieve existing File Attributes Data Type object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    FileDataTypeReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-data-type-file-attributes"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return FileDataTypeReply(**resp)
