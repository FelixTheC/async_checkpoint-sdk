from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class ContentAwarenessAdvancedSettingsRequestEdit(BaseModel):
    internal_error_fail_mode: str = Field(
        alias="internal-error-fail-mode",
        description="""In case of internal system error, allow or block all connections.""",
    )
    supported_services: Add | Remove | str | list[str] = Field(
        alias="supported-services",
        description="""Specify the services that Content Awareness inspects.""",
    )
    httpi_non_standard_ports: bool = Field(
        alias="httpi-non-standard-ports",
        description="""Servers usually send HTTP traffic on TCP port 80. Some servers send HTTP traffic on other ports also. By default, this setting is enabled and Content Awareness inspects HTTP traffic on non-standard ports. You can disable this setting and configure Content Awareness to inspect HTTP traffic only on port 80.""",
    )
    inspect_archives: bool = Field(
        alias="inspect-archives",
        description="""Examine the content of archive files. For example, files with the extension .zip, .gz, .tgz, .tar.Z, .tar, .lzma, .tlz, 7z, .rar.""",
    )
