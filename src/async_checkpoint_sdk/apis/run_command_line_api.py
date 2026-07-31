from aiohttp import ClientSession

from async_checkpoint_sdk.models.command_line_reply import CommandLineReply
from async_checkpoint_sdk.models.command_line_request import CommandLineRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def run_command_line(
    client: ClientSession, data: CommandLineRequest, config: SDKConfig, **kwargs
) -> CommandLineReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CommandLineRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CommandLineReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-command-line"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CommandLineReply(**resp)
