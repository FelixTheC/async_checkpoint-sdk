from pydantic import BaseModel, Field


class PolicyInstallationRequest(BaseModel):
    policy_package: str = Field(
        alias="policy-package", description="""The name of the Policy Package to be installed."""
    )
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. In case 'Specific gateways' is chosen, input installation targets must be in the specific targets list of the policy package. Targets may be identified by their name or object unique identifier.""",
    )
    access: bool = Field(
        alias="access",
        description="""Set to be true in order to install the Access Control policy. By default, the value is true if Access Control policy is enabled on the input policy package, otherwise false.""",
    )
    desktop_security: bool = Field(
        alias="desktop-security",
        description="""Set to be true in order to install the Desktop Security policy. By default, the value is true if desktop security policy is enabled on the input policy package, otherwise false.""",
    )
    qos: bool = Field(
        alias="qos",
        description="""Set to be true in order to install the QoS policy. By default, the value is true if Quality-of-Service policy is enabled on the input policy package, otherwise false.""",
    )
    threat_prevention: bool = Field(
        alias="threat-prevention",
        description="""Set to be true in order to install the Threat Prevention policy. By default, the value is true if Threat Prevention policy is enabled on the input policy package, otherwise false.""",
    )
    install_on_all_cluster_members_or_fail: bool = Field(
        alias="install-on-all-cluster-members-or-fail",
        description="""Relevant for the gateway clusters. If true, the policy is installed on all the cluster members. If the installation on a cluster member fails, don't install on that cluster.""",
    )
    prepare_only: bool = Field(
        alias="prepare-only",
        description="""If true, prepares the policy for the installation, but doesn't install it on an installation target.""",
    )
    revision: str = Field(
        alias="revision", description="""The UID of the revision of the policy to install."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Install policy ignoring policy mismatch warnings."""
    )
