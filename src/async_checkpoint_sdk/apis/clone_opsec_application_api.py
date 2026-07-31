from aiohttp import ClientSession

from async_checkpoint_sdk.models.opsec_application_reply import OpsecApplicationReply
from async_checkpoint_sdk.models.opsec_application_request_edit import OpsecApplicationRequestEdit
from config import Config


async def clone_opsec_application(
    client: ClientSession, data: OpsecApplicationRequestEdit, config: Config, **kwargs
) -> OpsecApplicationReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : OpsecApplicationRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OpsecApplicationReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-opsec-application"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OpsecApplicationReply(**resp)
