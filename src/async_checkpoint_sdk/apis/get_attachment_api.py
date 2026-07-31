from aiohttp import ClientSession

from async_checkpoint_sdk.models.packet_capture_reply import PacketCaptureReply
from async_checkpoint_sdk.models.packet_capture_request import PacketCaptureRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def get_attachment(
    client: ClientSession, data: PacketCaptureRequest, config: SDKConfig, **kwargs
) -> PacketCaptureReply:
    """
    Retrieves a packet capture or blob data, according to the attributes of a log record.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : PacketCaptureRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PacketCaptureReply
    data : PacketCaptureRequest [Argument]
        data : PacketCaptureRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PacketCaptureReply
    data : PacketCaptureRequest [Argument]
        data : PacketCaptureRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PacketCaptureReply
    """
    url = f"https://{config.server}:{config.port}/web_api/get-attachment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PacketCaptureReply(**resp)
