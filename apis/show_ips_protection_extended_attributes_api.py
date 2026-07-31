from config import Config
from aiohttp import ClientSession
from models.cds_ignore_query_request import CdsIgnoreQueryRequest
from models.ips_additional_properties_query_reply import IpsAdditionalPropertiesQueryReply


async def show_ips_protection_extended_attributes(
    client: ClientSession, data: CdsIgnoreQueryRequest, config: Config, **kwargs
) -> IpsAdditionalPropertiesQueryReply:
    """
    Retrieve all objects.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CdsIgnoreQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IpsAdditionalPropertiesQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ips-protection-extended-attributes"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IpsAdditionalPropertiesQueryReply(**resp)
