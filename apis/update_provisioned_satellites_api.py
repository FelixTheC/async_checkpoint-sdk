from config import Config
from aiohttp import ClientSession
from models.update_provisioned_satellites_request import UpdateProvisionedSatellitesRequest
from models.lsm_base_command_reply import LsmBaseCommandReply


async def update_provisioned_satellites(
    client: ClientSession, data: UpdateProvisionedSatellitesRequest, config: Config, **kwargs
) -> LsmBaseCommandReply:
    """
    Executes the update-provisioned-satellites on center gateways of VPN communities.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UpdateProvisionedSatellitesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LsmBaseCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/update-provisioned-satellites"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmBaseCommandReply(**resp)
