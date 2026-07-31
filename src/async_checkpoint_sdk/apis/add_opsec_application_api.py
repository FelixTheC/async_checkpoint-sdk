from aiohttp import ClientSession

from async_checkpoint_sdk.models.opsec_application_reply import OpsecApplicationReply
from async_checkpoint_sdk.models.opsec_application_request_new import OpsecApplicationRequestNew
from config import Config


async def add_opsec_application(
    client: ClientSession, data: OpsecApplicationRequestNew, config: Config, **kwargs
) -> OpsecApplicationReply:
    """
    Create a new OPSEC Application. At least one client entity (LEA, CPMI) must be supplied.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : OpsecApplicationRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OpsecApplicationReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-opsec-application"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OpsecApplicationReply(**resp)
