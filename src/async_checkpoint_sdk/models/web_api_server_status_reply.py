from .pydantic import BaseModel, Field


class WebApiServerStatusReply(BaseModel):
    api_more_info: str = Field(alias="api-more-info", description="""N/A""")
    api_overall_status: bool = Field(alias="api-overall-status", description="""N/A""")
    api_pid: str = Field(alias="api-pid", description="""N/A""")
    api_state: str = Field(alias="api-state", description="""N/A""")
    api_status: str = Field(alias="api-status", description="""N/A""")
    cpm_more_info: str = Field(alias="cpm-more-info", description="""N/A""")
    cpm_pid: str = Field(alias="cpm-pid", description="""N/A""")
    cpm_state: str = Field(alias="cpm-state", description="""N/A""")
    fwm_more_info: str = Field(alias="fwm-more-info", description="""N/A""")
    fwm_pid: str = Field(alias="fwm-pid", description="""N/A""")
    fwm_state: str = Field(alias="fwm-state", description="""N/A""")
    task_id: str = Field(
        alias="task-id",
        description="""Asynchronous task unique identifier. Use show-task command to check the progress of the task.""",
    )
