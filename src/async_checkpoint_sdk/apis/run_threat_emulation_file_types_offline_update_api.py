from aiohttp import ClientSession

from async_checkpoint_sdk.models.threat_emulation_file_types_update_reply import (
    ThreatEmulationFileTypesUpdateReply,
)
from async_checkpoint_sdk.models.threat_emulation_file_types_update_request import (
    ThreatEmulationFileTypesUpdateRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def run_threat_emulation_file_types_offline_update(
    client: ClientSession, data: ThreatEmulationFileTypesUpdateRequest, config: SDKConfig, **kwargs
) -> ThreatEmulationFileTypesUpdateReply:
    """
    Update Threat Emulation file types offline.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatEmulationFileTypesUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatEmulationFileTypesUpdateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-threat-emulation-file-types-offline-update"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatEmulationFileTypesUpdateReply(**resp)
