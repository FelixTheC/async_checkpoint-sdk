from aiohttp import ClientSession

from async_checkpoint_sdk.models.trust_request_base import TrustRequestBase
from async_checkpoint_sdk.models.trust_status_reply import TrustStatusReply
from config import Config


async def reset_trust(
    client: ClientSession, data: TrustRequestBase, config: Config, **kwargs
) -> TrustStatusReply:
    """
    Reset an existing Trusted communication between the Management Server and the managed Security Gateway<br><br><b>Procedure to reset Trusted communication</b><br><br>1) On the Management Server, use the API call "reset-trust" to reset the SIC with the managed Security Gateway.<br>2) On the managed Security Gateway:<br>&emsp;A) Connect to the command.<br>&emsp;B) Run: cpconfig<br>&emsp;C) Enter the number of the option "Secure Internal Communication" and follow the instructions on the screen.<br>3) On the Management Server, configure the SIC with the managed Security Gateway in one of these ways:<br>&emsp; - Use the API call "set trust".<br>&emsp; - Use the API call "set" for the applicable object - "set-simple-gateway", "set-simple-cluster", "set-checkpoint-host".<br>&emsp;Use the parameter "one-time-password" to configure the Activation Key you entered in the "cpconfig" menu.<br>4) On the Management Server, use the API call "test-trust" to examine the SIC with the managed Security Gateway.<br>&emsp; - The returned status represents the state of the Security Gateway after it received the certificate issued by the Internal CA on the Management Server.<br>&emsp; - The SIC status "Unknown" means there is no connection between the Management Server and the Security Gateway.<br>&emsp; - The SIC status "No Communication" means there is an issue. The corresponding error message can contain specific instructions to resolve this issue.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustRequestBase [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustStatusReply
    config : Config [Argument]
        data : TrustRequestBase [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustStatusReply
    config : Config [Argument]
        data : TrustRequestBase [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/reset-trust"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustStatusReply(**resp)
