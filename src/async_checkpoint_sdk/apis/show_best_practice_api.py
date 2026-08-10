from aiohttp import ClientSession

from async_checkpoint_sdk.models.compliance_best_practice_request_show import (
    ComplianceBestPracticeRequestShow,
)
from async_checkpoint_sdk.models.compliance_show_best_practice_reply import (
    ComplianceShowBestPracticeReply,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_best_practice(
    client: ClientSession, data: ComplianceBestPracticeRequestShow, config: SDKConfig, **kwargs
) -> ComplianceShowBestPracticeReply:
    """
    Retrieve existing Best Practice using object name, uid or best practice id.

    Parameters
    ----------
    client : ClientSession
    data : ComplianceBestPracticeRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ComplianceShowBestPracticeReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-best-practice"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceShowBestPracticeReply(**resp)
