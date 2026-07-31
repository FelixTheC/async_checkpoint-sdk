from aiohttp import ClientSession

from async_checkpoint_sdk.models.layer_structure_reply import LayerStructureReply
from async_checkpoint_sdk.models.layer_structure_request import LayerStructureRequest
from config import Config


async def show_layer_structure(
    client: ClientSession, data: LayerStructureRequest, config: Config, **kwargs
) -> LayerStructureReply:
    """
    Shows the entire layer structure. The layer structure is divided into sections and each section has its own entities.<br>Supported layer types: Access Control, NAT, Custom Threat Prevention, Threat Exception and HTTPS Inspection.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LayerStructureRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LayerStructureReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-layer-structure"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LayerStructureReply(**resp)
