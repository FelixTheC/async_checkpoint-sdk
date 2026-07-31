from aiohttp import ClientSession

from async_checkpoint_sdk.models.compliance_gaia_best_practice_reply import (
    ComplianceGaiaBestPracticeReply,
)
from async_checkpoint_sdk.models.compliance_gaia_best_practice_request_set import (
    ComplianceGaiaBestPracticeRequestSet,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_gaia_best_practice(
    client: ClientSession, data: ComplianceGaiaBestPracticeRequestSet, config: SDKConfig, **kwargs
) -> ComplianceGaiaBestPracticeReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ComplianceGaiaBestPracticeRequestSet [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ComplianceGaiaBestPracticeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-gaia-best-practice"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceGaiaBestPracticeReply(**resp)
