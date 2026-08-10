from aiohttp import ClientSession

from async_checkpoint_sdk.models.show_rule_candidate_reply import ShowRuleCandidateReply
from async_checkpoint_sdk.models.show_rule_candidate_request import ShowRuleCandidateRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_rule_candidates(
    client: ClientSession, data: ShowRuleCandidateRequest, config: SDKConfig, **kwargs
) -> ShowRuleCandidateReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : ShowRuleCandidateRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ShowRuleCandidateReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-rule-candidates"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowRuleCandidateReply(**resp)
