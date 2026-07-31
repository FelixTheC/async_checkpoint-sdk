from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.generic_object_identifier_request import (
    GenericObjectIdentifierRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_generic_object(
    client: ClientSession, data: GenericObjectIdentifierRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GenericObjectIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-generic-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
