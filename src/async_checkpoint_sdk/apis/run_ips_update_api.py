from aiohttp import ClientSession

from async_checkpoint_sdk.models.ips_update_reply import IpsUpdateReply
from async_checkpoint_sdk.models.ips_update_request import IpsUpdateRequest
from config import Config


async def run_ips_update(
    client: ClientSession, data: IpsUpdateRequest, config: Config, **kwargs
) -> IpsUpdateReply:
    """
    Runs IPS database update. If "package-path" is not provided server will try to get the latest package from the User Center.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : IpsUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IpsUpdateReply
    data : IpsUpdateRequest [Argument]
        data : IpsUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IpsUpdateReply
    data : IpsUpdateRequest [Argument]
        data : IpsUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IpsUpdateReply
    data : IpsUpdateRequest [Argument]
        data : IpsUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IpsUpdateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-ips-update"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IpsUpdateReply(**resp)
