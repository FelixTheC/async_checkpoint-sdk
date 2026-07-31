from aiohttp import ClientSession

from async_checkpoint_sdk.models.verify_lic_reply import VerifyLicReply
from async_checkpoint_sdk.models.verify_lic_request import VerifyLicRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def verify_management_license(
    client: ClientSession, data: VerifyLicRequest, config: SDKConfig, **kwargs
) -> VerifyLicReply:
    """
    Check how many Security Gateway objects the Management Server license supports.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : VerifyLicRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VerifyLicReply
    """
    url = f"https://{config.server}:{config.port}/web_api/verify-management-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VerifyLicReply(**resp)
