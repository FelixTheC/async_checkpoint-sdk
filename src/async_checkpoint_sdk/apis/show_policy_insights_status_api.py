from aiohttp import ClientSession

from async_checkpoint_sdk.models.afw_control_request import AfwControlRequest
from async_checkpoint_sdk.models.afw_control_status_reply import AfwControlStatusReply
from config import Config


async def show_policy_insights_status(
    client: ClientSession, data: AfwControlRequest, config: Config, **kwargs
) -> AfwControlStatusReply:
    """
    Retrieve the current state of Policy Insights, including enablement and supported API versions.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AfwControlRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AfwControlStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-policy-insights-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AfwControlStatusReply(**resp)
