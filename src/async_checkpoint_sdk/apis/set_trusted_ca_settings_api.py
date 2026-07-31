from aiohttp import ClientSession

from async_checkpoint_sdk.models.trusted_ca_settings_reply import TrustedCaSettingsReply
from async_checkpoint_sdk.models.trusted_ca_settings_request_edit import (
    TrustedCaSettingsRequestEdit,
)
from config import Config


async def set_trusted_ca_settings(
    client: ClientSession, data: TrustedCaSettingsRequestEdit, config: Config, **kwargs
) -> TrustedCaSettingsReply:
    """
    Set trusted CAs package automatic update settings.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustedCaSettingsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustedCaSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-trusted-ca-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaSettingsReply(**resp)
