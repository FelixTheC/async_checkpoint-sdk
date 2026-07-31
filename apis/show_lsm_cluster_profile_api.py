from config import Config
from aiohttp import ClientSession
from models.lsm_cluster_profile_reply import LsmClusterProfileReply
from models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)


async def show_lsm_cluster_profile(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> LsmClusterProfileReply:
    """
    Show LSM Gateway Profile.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LsmClusterProfileReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-lsm-cluster-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmClusterProfileReply(**resp)
