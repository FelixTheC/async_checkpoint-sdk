from .cluster_installation_settings import ClusterInstallationSettings
from .pydantic import BaseModel, Field


class DeploymentCommandRequestVerify(BaseModel):
    cluster_installation_settings: ClusterInstallationSettings = Field(
        alias="cluster-installation-settings",
        description="""Installation settings for cluster.""",
    )
    concurrency_limit: int = Field(
        alias="concurrency-limit",
        description="""The number of targets, on which the same package is installed at the same time.""",
    )
    download_package: bool = Field(
        alias="download-package",
        description="""Should the package be downloaded before verification.""",
    )
    download_package_from: str = Field(
        alias="download-package-from", description="""Where is the package located."""
    )
    operation_context: str = Field(
        alias="operation-context",
        description="""The operation can be: 'install' (default) or 'uninstall'.""",
    )
