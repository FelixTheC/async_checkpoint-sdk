from pydantic import BaseModel, Field
from restrictions import Restrictions
from supported_blades import SupportedBlades
from supported_firmware_platforms import SupportedFirmwarePlatforms
from supported_hardware import SupportedHardware
from supported_hardware_subtypes import SupportedHardwareSubtypes
from supported_platforms import SupportedPlatforms
from supported_versions import SupportedVersions


class GatewayCapabilitiesReply(BaseModel):
    restrictions: Restrictions = Field(
        alias="restrictions", description="""Set of restrictions."""
    )
    supported_blades: SupportedBlades = Field(
        alias="supported-blades",
        description="""Supported blades according to restrictions.""",
    )
    supported_firmware_platforms: SupportedFirmwarePlatforms = Field(
        alias="supported-firmware-platforms",
        description="""Supported firmware platforms according to restrictions.""",
    )
    supported_hardware: SupportedHardware = Field(
        alias="supported-hardware",
        description="""Supported hardware according to restrictions.""",
    )
    supported_hardware_subtypes: SupportedHardwareSubtypes = Field(
        alias="supported-hardware-subtypes",
        description="""Supported hardware-subtypes according to restrictions.""",
    )
    supported_platforms: SupportedPlatforms = Field(
        alias="supported-platforms",
        description="""Supported platforms according to restrictions.""",
    )
    supported_versions: SupportedVersions = Field(
        alias="supported-versions",
        description="""Supported versions according to restrictions.""",
    )
