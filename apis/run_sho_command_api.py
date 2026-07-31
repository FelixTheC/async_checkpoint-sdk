from config import Config
from aiohttp import ClientSession
from models.sho_cmd_reply import ShoCmdReply
from models.sho_cmd_request import ShoCmdRequest


async def run_sho_command(
    client: ClientSession, data: ShoCmdRequest, config: Config, **kwargs
) -> ShoCmdReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShoCmdRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ShoCmdReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-sho-command"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShoCmdReply(**resp)
