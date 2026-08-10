from aiohttp import ClientSession

from async_checkpoint_sdk.models.scada_application_reply import ScadaApplicationReply
from async_checkpoint_sdk.models.scada_application_request_edit import ScadaApplicationRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_scada_application(
    client: ClientSession, data: ScadaApplicationRequestEdit, config: SDKConfig, **kwargs
) -> ScadaApplicationReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ScadaApplicationRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ScadaApplicationReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-scada-application"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScadaApplicationReply(**resp)
