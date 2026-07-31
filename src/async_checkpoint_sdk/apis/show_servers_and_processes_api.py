from aiohttp import ClientSession

from async_checkpoint_sdk.models.mds_stat_reply import MdsStatReply
from async_checkpoint_sdk.models.mds_stat_request import MdsStatRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_servers_and_processes(
    client: ClientSession, data: MdsStatRequest, config: SDKConfig, **kwargs
) -> MdsStatReply:
    """
    Shows the status of all processes in the current machine (Multi-Domain Server and all Domain Management / Log Servers). <br>This command is available only on Multi-Domain Server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MdsStatRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MdsStatReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-servers-and-processes"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdsStatReply(**resp)
