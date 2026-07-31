from config import Config
from aiohttp import ClientSession
from models.clone_object_reply import CloneObjectReply
from models.clone_object_request import CloneObjectRequest


async def clone_object(
    client: ClientSession, data: CloneObjectRequest, config: Config, **kwargs
) -> CloneObjectReply:
    """
    Creates a clone of an existing object.  <br>Clone supported types: access-role, address-range, application-site-category, application-site-group, dns-domain, dynamic-object, group, group-with-exclusion, host, lsv-profile, multicast-address-range, network, security-zone, service-dce-rpc, service-group, service-icmp, service-other, service-sctp, service-tcp, service-udp, tacacs-server, tacacs-group, tag, time, time-group, vpn-community-meshed, vpn-community-star, wildcard.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloneObjectRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CloneObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CloneObjectReply(**resp)
