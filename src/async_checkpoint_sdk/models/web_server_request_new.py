from .pydantic import BaseModel, Field


class WebServerRequestNew(BaseModel):
    additional_ports: str | list[str] = Field(
        alias="additional-ports", description="""Server additional ports."""
    )
    application_engines: str | list[str] = Field(
        alias="application-engines",
        description="""Application engines of this web server.""",
    )
    listen_standard_port: bool = Field(
        alias="listen-standard-port",
        description="""Whether server listens to standard port.""",
    )
    operating_system: str = Field(alias="operating-system", description="""Operating System.""")
    protected_by: str = Field(
        alias="protected-by",
        description="""Network object which protects this server identified by the name or UID.""",
    )
