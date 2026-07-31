from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_base_command_reply import LsmBaseCommandReply
from async_checkpoint_sdk.models.lsm_install_settings_request import LsmInstallSettingsRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def install_lsm_settings(
    client: ClientSession, data: LsmInstallSettingsRequest, config: SDKConfig, **kwargs
) -> LsmBaseCommandReply:
    """
    Executes the lsm-install-settings on a given list of targets. Install the provisioning settings that defined on the object on the targets devices.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LsmInstallSettingsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LsmBaseCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/install-lsm-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmBaseCommandReply(**resp)
