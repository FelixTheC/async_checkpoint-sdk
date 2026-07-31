from aiohttp import ClientSession

from async_checkpoint_sdk.models.sho_cmd_reply import ShoCmdReply
from async_checkpoint_sdk.models.sho_cmd_request import ShoCmdRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def run_sho_command(
    client: ClientSession, data: ShoCmdRequest, config: SDKConfig, **kwargs
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
