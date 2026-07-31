from cluster_installation_settings import ClusterInstallationSettings
from pydantic import BaseModel, Field


class DeploymentCommandRequest(BaseModel):
    name: str = Field(alias="name", description="""The name of the software package.""")
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier.""",
    )
    cluster_installation_settings: ClusterInstallationSettings = Field(
        alias="cluster-installation-settings", description="""Installation settings for cluster."""
    )
    concurrency_limit: int = Field(
        alias="concurrency-limit",
        description="""The number of targets, on which the same package is installed at the same time.""",
    )
