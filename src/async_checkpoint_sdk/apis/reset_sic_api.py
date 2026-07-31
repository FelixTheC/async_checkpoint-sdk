from aiohttp import ClientSession

from async_checkpoint_sdk.models.reset_sic_reply import ResetSicReply
from async_checkpoint_sdk.models.sic_api_request import SicApiRequest
from config import Config


async def reset_sic(
    client: ClientSession, data: SicApiRequest, config: Config, **kwargs
) -> ResetSicReply:
    """
    <br>Reset the Secure Internal Communication (SIC).<br><br>Follow these steps:<br><br>1. Use this 'reset-sic' API to reset SIC on the Management Server in the device object.<br>2. On the device, run the 'cpconfig' command (in Gaia Clish or Expert mode).<br>&emsp;In the menu select 'Secure Internal Communication', and follow the instructions on the screen.<br>&emsp;Save the Activation Key you used.<br>3. Establish SIC between the Management Server and the device.<br>&emsp;Use the 'set' API of the applicable object (set-simple-gateway, set-simple-cluster, set-checkpoint-host).<br>&emsp;Use the Activation Key you configured on the device as the 'one-time-password' parameter in the 'set' API.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SicApiRequest [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ResetSicReply
    config : Config [Argument]
        data : SicApiRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ResetSicReply
    config : Config [Argument]
        data : SicApiRequest [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ResetSicReply
    """
    url = f"https://{config.server}:{config.port}/web_api/reset-sic"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ResetSicReply(**resp)
