from aiohttp import ClientSession

from async_checkpoint_sdk.models.onboarding_data_reply import OnboardingDataReply
from async_checkpoint_sdk.models.onboarding_data_request import OnboardingDataRequest
from config import Config


async def show_gateways_onboarding_data(
    client: ClientSession, data: OnboardingDataRequest, config: Config, **kwargs
) -> OnboardingDataReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : OnboardingDataRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OnboardingDataReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-gateways-onboarding-data"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OnboardingDataReply(**resp)
