from .pydantic import BaseModel, Field


class ClusterInstallationSettings(BaseModel):
    cluster_delay: int = Field(
        alias="cluster-delay",
        description="""The delay between end of installation on one cluster members and start of installation on the next cluster member.""",
    )
    cluster_strategy: str = Field(
        alias="cluster-strategy",
        description="""The cluster installation strategy.
all-members - Install the package on all members in the cluster
non-active-members-and-failover - In the High Availability cluster, install the package only on the selected cluster members with the cluster state 'Standby' and then failover from .the current 'Active' member to one of the updated members
non-active-members-no-failover - In the High Availability cluster, install the package only on the selected cluster members with the cluster state 'Standby' and then do not failover from .the current 'Active' member to one of the updated members.""",
    )
