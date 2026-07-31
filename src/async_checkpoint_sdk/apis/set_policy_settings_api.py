from aiohttp import ClientSession

from async_checkpoint_sdk.models.policy_settings_reply import PolicySettingsReply
from async_checkpoint_sdk.models.policy_settings_request_edit import PolicySettingsRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_policy_settings(
    client: ClientSession, data: PolicySettingsRequestEdit, config: SDKConfig, **kwargs
) -> PolicySettingsReply:
    """
    Edit Policy settings, the changes will be applied after publish.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : PolicySettingsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PolicySettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-policy-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PolicySettingsReply(**resp)
