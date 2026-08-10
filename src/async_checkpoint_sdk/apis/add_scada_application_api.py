from aiohttp import ClientSession

from async_checkpoint_sdk.models.scada_application_reply import ScadaApplicationReply
from async_checkpoint_sdk.models.scada_application_request_new import ScadaApplicationRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_scada_application(
    client: ClientSession, data: ScadaApplicationRequestNew, config: SDKConfig, **kwargs
) -> ScadaApplicationReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : ScadaApplicationRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ScadaApplicationReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-scada-application"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScadaApplicationReply(**resp)
