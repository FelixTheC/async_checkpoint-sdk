from aiohttp import ClientSession

from async_checkpoint_sdk.models.verify_policy_reply import VerifyPolicyReply
from async_checkpoint_sdk.models.verify_policy_request import VerifyPolicyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def verify_policy(
    client: ClientSession, data: VerifyPolicyRequest, config: SDKConfig, **kwargs
) -> VerifyPolicyReply:
    """
    Verifies the policy of the selected package. <br>Note: Verify Policy command can verify only access policy.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : VerifyPolicyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VerifyPolicyReply
    """
    url = f"https://{config.server}:{config.port}/web_api/verify-policy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VerifyPolicyReply(**resp)
