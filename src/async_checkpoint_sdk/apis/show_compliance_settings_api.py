from aiohttp import ClientSession

from async_checkpoint_sdk.models.compliance_configuration_settings_show_request import (
    ComplianceConfigurationSettingsShowRequest,
)
from async_checkpoint_sdk.models.compliance_show_configuration_settings_reply import (
    ComplianceShowConfigurationSettingsReply,
)
from config import Config


async def show_compliance_settings(
    client: ClientSession,
    data: ComplianceConfigurationSettingsShowRequest,
    config: Config,
    **kwargs,
) -> ComplianceShowConfigurationSettingsReply:
    """
    Retrieve all Compliance Settings.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ComplianceConfigurationSettingsShowRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ComplianceShowConfigurationSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-compliance-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceShowConfigurationSettingsReply(**resp)
