from .pydantic import BaseModel, Field


class ConnectControlGlobalPropertiesReply(BaseModel):
    load_agents_port: int = Field(
        alias="load-agents-port",
        description="""Sets the port number on which load measuring agents communicate with ConnectControl.""",
    )
    load_measurement_interval: int = Field(
        alias="load-measurement-interval",
        description="""sets how often (in seconds) the load measuring agents report their load status to ConnectControl.""",
    )
    persistence_server_timeout: int = Field(
        alias="persistence-server-timeout",
        description="""Sets the amount of time (in seconds) that a client, once directed to a particular server, will continue to be directed to that same server.""",
    )
    server_availability_check_interval: int = Field(
        alias="server-availability-check-interval",
        description="""Sets how often (in seconds) ConnectControl checks to make sure the load balanced servers are running and responding to service requests.""",
    )
    server_check_retries: int = Field(
        alias="server-check-retries",
        description="""Sets how many times ConnectControl attempts to contact a server before ceasing to direct traffic to it.""",
    )
