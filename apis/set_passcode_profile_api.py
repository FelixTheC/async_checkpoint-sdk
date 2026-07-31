from config import Config
from aiohttp import ClientSession
from models.passcode_profile_reply import PasscodeProfileReply
from models.passcode_profile_request_edit import PasscodeProfileRequestEdit


async def set_passcode_profile(
    client: ClientSession, data: PasscodeProfileRequestEdit, config: Config, **kwargs
) -> PasscodeProfileReply:
    """
    Edit existing Passcode Profile using name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PasscodeProfileRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
