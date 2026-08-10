from aiohttp import ClientSession

from async_checkpoint_sdk.models.passcode_profile_reply import PasscodeProfileReply
from async_checkpoint_sdk.models.passcode_profile_request_edit import PasscodeProfileRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_passcode_profile(
    client: ClientSession, data: PasscodeProfileRequestEdit, config: SDKConfig, **kwargs
) -> PasscodeProfileReply:
    """
    Edit existing Passcode Profile using name or uid.

    Parameters
    ----------
    client : ClientSession
    data : PasscodeProfileRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    PasscodeProfileReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-passcode-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PasscodeProfileReply(**resp)
