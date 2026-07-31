from pydantic import BaseModel, Field


class QueryObjectsRequest(BaseModel):
    uids: list[str] = Field(
        alias="uids", description="""List of UIDs of the objects to retrieve."""
    )
    filter: str = Field(
        alias="filter",
        description="""Search expression to filter objects by. The provided text should be exactly the same as it would be given in Smart Console. The logical operators in the expression ('AND', 'OR') should be provided in capital letters. By default, the search involves both a textual search and a IP search. To use IP search only, set the ip-only parameter to true.""",
    )
    ip_only: bool = Field(
        alias="ip-only",
        description="""If using filter, use this field to search objects by their IP address only, without involving the textual search.<br><br>IP search use cases<br>&nbsp;&nbsp;&nbsp;&nbsp; <ul><li>Full IPv4 address matches for:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Check Point Hosts and Gateways with exact IPv4 match or with interfaces which subnet contains the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - IPv4 Networks and IPv4 Address Ranges that contain the search address</li> <br>&nbsp;&nbsp;&nbsp;&nbsp; <li>Partial IPv4 address matches for:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Networks, Check Point Hosts and Gateways with IPv4 address that starts from the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Check Point Hosts and Gateways with interfaces which subnet address starts from the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - IPv4 Address Ranges with first address or last address that starts from the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - IPv4 Networks and IPv4 Address Ranges that contain the network derived from the search address supplemented with missing octets (all zeroes)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Check Point Hosts and Gateways with interfaces which subnet contains the network derived from the search address supplemented with missing octets (all zeroes)</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li>IPv6 address:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Not supported</li></ul><br><br> * Check Point Host is a server of type Network Policy Management, Logging & Status, SmartEvent, etc.<br> * When one IP address is checked to start from another (partial) IP address - only full octets are considered <br> * Check Examples part for IP search examples.""",
    )
    limit: int = Field(alias="limit", description="""The maximal number of returned results.""")
    offset: int = Field(alias="offset", description="""Number of the results to initially skip.""")
    order: list[dict] = Field(
        alias="order",
        description="""Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order.""",
    )
    type: str = Field(
        alias="type",
        description="""The objects' type, e.g.: host, service-tcp, network, address-range...""",
    )
    dereference_group_members: bool = Field(
        alias="dereference-group-members",
        description="""Indicates whether to dereference members field by details level for every object in reply.""",
    )
    show_membership: bool = Field(
        alias="show-membership",
        description="""Indicates whether to calculate and show groups field for every object in reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    show_only_local_domain: bool = Field(
        alias="show-only-local-domain",
        description="""Indicates whether the query should return only objects from the current local domain. This parameter is only valid for local domain.""",
    )
