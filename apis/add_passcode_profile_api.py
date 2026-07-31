from config import Config
from aiohttp import ClientSession
from models.passcode_profile_request_new import PasscodeProfileRequestNew
from models.passcode_profile_reply import PasscodeProfileReply


async def add_passcode_profile(
    client: ClientSession, data: PasscodeProfileRequestNew, config: Config, **kwargs
) -> PasscodeProfileReply:
    """
    Create new Passcode Profile for configurations Mobile Profile objects.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PasscodeProfileRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PasscodeProfileReply
    config : Config [Argument]
        data : PasscodeProfileRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PasscodeProfileReply
    config : Config [Argument]
        data : PasscodeProfileRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PasscodeProfileReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-passcode-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PasscodeProfileReply(**resp)
