from cluster_installation_settings import ClusterInstallationSettings
from pydantic import BaseModel, Field


class DeploymentCommandRequest(BaseModel):
    cluster_installation_settings: ClusterInstallationSettings = Field(
        alias="cluster-installation-settings",
        description="""Installation settings for cluster.""",
    )
    concurrency_limit: int = Field(
        alias="concurrency-limit",
        description="""The number of targets, on which the same package is installed at the same time.""",
    )
