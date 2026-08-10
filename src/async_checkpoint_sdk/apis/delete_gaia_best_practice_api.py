from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.compliance_gaia_best_practice_request_delete import (
    ComplianceGaiaBestPracticeRequestDelete,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_gaia_best_practice(
    client: ClientSession, data: ComplianceGaiaBestPracticeRequestDelete, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Delete a user-defined Gaia Best Practice.

    Parameters
    ----------
    client : ClientSession
    data : ComplianceGaiaBestPracticeRequestDelete
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiOkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/delete-gaia-best-practice"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
