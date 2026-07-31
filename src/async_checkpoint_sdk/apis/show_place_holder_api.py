from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_place_holder_identifier_request import (
    ApiPlaceHolderIdentifierRequest,
)
from async_checkpoint_sdk.models.api_place_holder_reply import ApiPlaceHolderReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_place_holder(
    client: ClientSession, data: ApiPlaceHolderIdentifierRequest, config: SDKConfig, **kwargs
) -> ApiPlaceHolderReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiPlaceHolderIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiPlaceHolderReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-place-holder"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiPlaceHolderReply(**resp)
