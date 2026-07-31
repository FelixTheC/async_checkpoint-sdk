from pydantic import BaseModel, Field


class CloneDomainRequest(BaseModel):
    name: str = Field(alias="name", description="""Name of the source Domain to clone.""")
    new_domain_name: str = Field(alias="new-domain-name", description="""Name of the new Domain.""")
    new_domain_server_name: str = Field(
        alias="new-domain-server-name", description="""Name of the new Domain Server."""
    )
    new_domain_server_ip: str = Field(
        alias="new-domain-server-ip", description="""IPv4 Address of the new Domain Server."""
    )
    new_domain_server_ipv6: str = Field(
        alias="new-domain-server-ipv6",
        description="""IPv6 Address of the new Domain Server.<br><font color=red>Required only if</font> the source Domain has an IPv6 address.""",
    )
    omit_sensitive_info: bool = Field(
        alias="omit-sensitive-info",
        description="""Remove sensitive information from exported database.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings",
        description="""Ignoring the verification warnings. By Setting this parameter to 'true' the clone will not be blocked by warnings.""",
    )
