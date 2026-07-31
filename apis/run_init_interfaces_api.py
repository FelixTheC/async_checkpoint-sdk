from config import Config
from aiohttp import ClientSession
from models.run_init_interfaces_request import RunInitInterfacesRequest
from models.run_init_interfaces_reply import RunInitInterfacesReply


async def run_init_interfaces(
    client: ClientSession, data: RunInitInterfacesRequest, config: Config, **kwargs
) -> RunInitInterfacesReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : RunInitInterfacesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    RunInitInterfacesReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-init-interfaces"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RunInitInterfacesReply(**resp)
