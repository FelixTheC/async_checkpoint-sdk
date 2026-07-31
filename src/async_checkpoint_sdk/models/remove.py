from pydantic import BaseModel, Field
from users_source_and_selection_request import UsersSourceAndSelectionRequest


class Remove(BaseModel):
    remove: UsersSourceAndSelectionRequest | list[dict] = Field(
        alias="remove", description="""Removes from collection of values"""
    )
