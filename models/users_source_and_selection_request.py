from pydantic import BaseModel, Field


class UsersSourceAndSelectionRequest(BaseModel):
    uid: str = Field(
        alias="uid",
        description="""When source is Azure Active Directory or Infinity Identity Provider use UID to refine the query in identity provider database.""",
    )
    base_dn: str = Field(
        alias="base-dn",
        description="""When source is Active Directory use base-dn to refine the query in AD database.""",
    )
