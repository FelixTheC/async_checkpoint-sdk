from pydantic import BaseModel, Field


class MachinesSourceAndSelectionRequest(BaseModel):
    source: str = Field(alias="source", description="""Active Directory name or Identity Tag.""")
    selection: str | list[str] = Field(
        alias="selection",
        description="""Name or UID of an object selected from source. When source is Azure Active Directory or Infinity Identity Provider the name should be as defined in the identity provider.""",
    )
    uid: str = Field(
        alias="uid",
        description="""When source is Azure Active Directory or Infinity Identity Provider use UID to refine the query in identity provider database.""",
    )
    base_dn: str = Field(
        alias="base-dn",
        description="""When source is Active Directory use base-dn to refine the query in AD database.""",
    )
