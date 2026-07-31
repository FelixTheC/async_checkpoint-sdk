from aiohttp import ClientSession

from async_checkpoint_sdk.models.compliance_configuration_settings_reply import (
    ComplianceConfigurationSettingsReply,
)
from async_checkpoint_sdk.models.compliance_configuration_settings_set_request import (
    ComplianceConfigurationSettingsSetRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_compliance_settings(
    client: ClientSession, data: ComplianceConfigurationSettingsSetRequest, config: SDKConfig, **kwargs
) -> ComplianceConfigurationSettingsReply:
    """
    Edit existing Compliance Settings.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ComplianceConfigurationSettingsSetRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ComplianceConfigurationSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-compliance-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceConfigurationSettingsReply(**resp)
