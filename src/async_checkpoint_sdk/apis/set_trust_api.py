from aiohttp import ClientSession

from async_checkpoint_sdk.models.set_trust_reply import SetTrustReply
from async_checkpoint_sdk.models.set_trust_request import SetTrustRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_trust(
    client: ClientSession, data: SetTrustRequest, config: SDKConfig, **kwargs
) -> SetTrustReply:
    """
    Configure a Trusted communication between the Management Server and the managed Security Gateway.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SetTrustRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SetTrustReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-trust"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SetTrustReply(**resp)
