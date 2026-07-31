from dynamic_object_request_new import DynamicObjectRequestNew
from pydantic import BaseModel, Field
from topology_request_new import TopologyRequestNew


class LsmClusterRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    main_ip_address: str = Field(alias="main-ip-address", description="""Main IP address.""")
    security_profile: str = Field(alias="security-profile", description="""LSM profile.""")
    dynamic_objects: DynamicObjectRequestNew | list[dict] = Field(
        alias="dynamic-objects", description="""Dynamic Objects."""
    )
    interfaces: list[dict] = Field(alias="interfaces", description="""Interfaces.""")
    members: list[dict] = Field(alias="members", description="""Cluster members.""")
    topology: TopologyRequestNew = Field(alias="topology", description="""Topology.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings",
        description="""Apply changes ignoring warnings. By Setting this parameter to 'true' SIC failure and using existing main ip-address will be ignored.""",
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
