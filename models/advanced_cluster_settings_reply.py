from pydantic import BaseModel, Field
from state_syncronization import StateSyncronization


class AdvancedClusterSettingsReply(BaseModel):
    member_recovery_mode: str = Field(
        alias="member-recovery-mode",
        description="""In a High Availability cluster, each member is given a priority. The member with the highest priority serves as the gateway. If this gateway fails, control is passed to the member with the next highest priority. If that member fails, control is passed to the next, and so on. Upon gateway recovery, it is possible to:
Maintain current active Cluster Member (maintain-current-active) or
Switch to higher priority Cluster Member (according-to-priority).""",
    )
    state_synchronization: StateSyncronization = Field(
        alias="state-synchronization",
        description="""Cluster State Synchronization settings.""",
    )
    track_changes_of_cluster_members: str = Field(
        alias="track-changes-of-cluster-members",
        description="""Track changes in the status of Cluster Members.""",
    )
    use_virtual_mac: bool = Field(
        alias="use-virtual-mac",
        description="""Use Virtual MAC. By enabling Virtual MAC in ClusterXL High Availability New mode, or Load Sharing Unicast mode, all cluster members associate the same Virtual MAC address with All Cluster Virtual Interfaces and the Virtual IP address.""",
    )
