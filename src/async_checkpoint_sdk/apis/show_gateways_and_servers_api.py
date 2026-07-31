from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_ignore_filter_and_live_request import (
    ApiQueryIgnoreFilterAndLiveRequest,
)
from async_checkpoint_sdk.models.query_gateways_servers_reply import QueryGatewaysServersReply
from config import Config


async def show_gateways_and_servers(
    client: ClientSession, data: ApiQueryIgnoreFilterAndLiveRequest, config: Config, **kwargs
) -> QueryGatewaysServersReply:
    """
    Shows list of Gateways & Servers sorted by name.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiQueryIgnoreFilterAndLiveRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    QueryGatewaysServersReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-gateways-and-servers"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return QueryGatewaysServersReply(**resp)
