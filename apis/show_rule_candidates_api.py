from config import Config
from aiohttp import ClientSession
from models.show_rule_candidate_request import ShowRuleCandidateRequest
from models.show_rule_candidate_reply import ShowRuleCandidateReply


async def show_rule_candidates(
    client: ClientSession, data: ShowRuleCandidateRequest, config: Config, **kwargs
) -> ShowRuleCandidateReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowRuleCandidateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
