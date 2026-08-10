from aiohttp import ClientSession

from async_checkpoint_sdk.models.trusted_ca_settings_reply import TrustedCaSettingsReply
from async_checkpoint_sdk.models.trusted_ca_settings_request_show import (
    TrustedCaSettingsRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_trusted_ca_settings(
    client: ClientSession, data: TrustedCaSettingsRequestShow, config: SDKConfig, **kwargs
) -> TrustedCaSettingsReply:
    """
    Show trusted CAs package update settings.

    Parameters
    ----------
    client : ClientSession
    data : TrustedCaSettingsRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TrustedCaSettingsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-trusted-ca-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaSettingsReply(**resp)
