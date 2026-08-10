from aiohttp import ClientSession

from async_checkpoint_sdk.models.turn_on_off_central_licenses_reply import (
    TurnOnOffCentralLicensesReply,
)
from async_checkpoint_sdk.models.turn_on_off_central_licenses_request import (
    TurnOnOffCentralLicensesRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def vsec_lic_cli(
    client: ClientSession, data: TurnOnOffCentralLicensesRequest, config: SDKConfig, **kwargs
) -> TurnOnOffCentralLicensesReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : TurnOnOffCentralLicensesRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TurnOnOffCentralLicensesReply

    """
    url = f"https://{config.server}:{config.port}/web_api/vsec-lic-cli"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TurnOnOffCentralLicensesReply(**resp)
