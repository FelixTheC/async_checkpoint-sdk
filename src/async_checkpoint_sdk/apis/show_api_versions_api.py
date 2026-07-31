from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_versions_reply import ApiVersionsReply
from async_checkpoint_sdk.models.empty_request import EmptyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_api_versions(
    client: ClientSession, data: EmptyRequest, config: SDKConfig, **kwargs
) -> ApiVersionsReply:
    """
    Shows all supported API versions and current API version (the latest one).

    Parameters
    ----------
    client : ClientSession [Argument]
    data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiVersionsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-api-versions"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiVersionsReply(**resp)
