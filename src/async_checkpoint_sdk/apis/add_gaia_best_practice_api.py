from aiohttp import ClientSession

from async_checkpoint_sdk.models.compliance_gaia_best_practice_reply import (
    ComplianceGaiaBestPracticeReply,
)
from async_checkpoint_sdk.models.compliance_gaia_best_practice_request_new import (
    ComplianceGaiaBestPracticeRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_gaia_best_practice(
    client: ClientSession, data: ComplianceGaiaBestPracticeRequestNew, config: SDKConfig, **kwargs
) -> ComplianceGaiaBestPracticeReply:
    """
    Add a new Gaia Best Practice with a custom script that runs on Gaia Security Gateways. <br/>During the Compliance scan, the practice script runs on the Gaia Security Gateway. To comply with the Best Practice, the script's output should match the expected output parameter.

    Parameters
    ----------
    client : ClientSession
    data : ComplianceGaiaBestPracticeRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ComplianceGaiaBestPracticeReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-gaia-best-practice"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceGaiaBestPracticeReply(**resp)
