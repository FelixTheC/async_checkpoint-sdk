from aiohttp import ClientSession

from async_checkpoint_sdk.models.compliance_gaia_best_practice_query_reply import (
    ComplianceGaiaBestPracticeQueryReply,
)
from async_checkpoint_sdk.models.compliance_gaia_best_practice_query_request import (
    ComplianceGaiaBestPracticeQueryRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_gaia_best_practices(
    client: ClientSession, data: ComplianceGaiaBestPracticeQueryRequest, config: SDKConfig, **kwargs
) -> ComplianceGaiaBestPracticeQueryReply:
    """
    Show all Gaia Best Practices.

    Parameters
    ----------
    client : ClientSession
    data : ComplianceGaiaBestPracticeQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ComplianceGaiaBestPracticeQueryReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-gaia-best-practices"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceGaiaBestPracticeQueryReply(**resp)
