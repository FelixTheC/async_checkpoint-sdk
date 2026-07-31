from config import Config
from aiohttp import ClientSession
from models.cdm_command_reply import CdmCommandReply
from models.put_file_request import PutFileRequest


async def put_file(
    client: ClientSession, data: PutFileRequest, config: Config, **kwargs
) -> CdmCommandReply:
    """
    Executes the put-file on a given list of targets.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PutFileRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CdmCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/put-file"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CdmCommandReply(**resp)
