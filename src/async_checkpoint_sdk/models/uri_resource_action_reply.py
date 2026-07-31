from .pydantic import BaseModel, Field


class UriResourceActionReply(BaseModel):
    replacement_uri: str = Field(
        alias="replacement-uri",
        description="""If the Action in a rule which uses this resource is Drop or Reject, then the Replacement URI is displayed instead of the one requested by the user.""",
    )
    strip_script_tags: bool = Field(
        alias="strip-script-tags", description="""Strip JAVA scripts."""
    )
    strip_applet_tags: bool = Field(
        alias="strip-applet-tags", description="""Strip JAVA applets."""
    )
    strip_activex_tags: bool = Field(
        alias="strip-activex-tags", description="""Strip activeX tags."""
    )
    strip_ftp_links: bool = Field(alias="strip-ftp-links", description="""Strip ftp links.""")
    strip_port_strings: bool = Field(alias="strip-port-strings", description="""Strip ports.""")
