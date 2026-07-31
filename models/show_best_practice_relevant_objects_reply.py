from pydantic import BaseModel, Field


class ShowBestPracticeRelevantObjectsReply(BaseModel):
    access_rules_info: list[dict] = Field(
        alias="access-rules-info",
        description="""The information about the relevant access rules. Appears only when the value of the 'relevant-objects-type' parameter is 'access-rule'.""",
    )
    cpm_relevant_objects_info: list[dict] = Field(
        alias="cpm-relevant-objects-info",
        description="""The information about the relevant objects. Appears only when the value of the 'relevant-objects-type' parameter is 'cpm-relevant-object'.""",
    )
    ips_protections_info: list[dict] = Field(
        alias="ips-protections-info",
        description="""The information about the relevant ips-protection objects. Appears only when the value of the 'relevant-objects-type' parameter is 'ips-protection'.""",
    )
    relevant_objects_type: str = Field(
        alias="relevant-objects-type",
        description="""The type of the relevant object.""",
    )
