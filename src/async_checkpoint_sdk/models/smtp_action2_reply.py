from pydantic import BaseModel, Field


class SmtpAction2Reply(BaseModel):
    strip_mime_of_type: str = Field(
        alias="strip-mime-of-type",
        description="""Specifies the MIME type to strip from the message.""",
    )
    strip_file_by_name: str = Field(
        alias="strip-file-by-name",
        description="""Strips file attachments of the specified name from the message.""",
    )
    mail_capacity: int = Field(
        alias="mail-capacity",
        description="""Restrict the size (in kb) of incoming email attachments.""",
    )
    allowed_characters: str = Field(
        alias="allowed-characters",
        description="""The MIME email headers can consist of 8 or 7 bit characters (7 ASCII and 8 for sending Binary characters) in order to encode mail data.""",
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
