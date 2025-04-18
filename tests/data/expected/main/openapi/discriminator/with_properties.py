# generated by datamodel-codegen:
#   filename:  discriminator_with_properties.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Literal, Optional, Union

from pydantic import BaseModel, Field, RootModel


class UserContextVariable(BaseModel):
    accountId: str = Field(..., description='The account ID of the user.')
    field_type: str = Field(
        ..., alias='@type', description='Type of custom context variable.'
    )


class IssueContextVariable(BaseModel):
    id: Optional[int] = Field(None, description='The issue ID.')
    key: Optional[str] = Field(None, description='The issue key.')
    field_type: str = Field(
        ..., alias='@type', description='Type of custom context variable.'
    )


class CustomContextVariable1(UserContextVariable):
    field_type: Literal['user'] = Field(
        ..., alias='@type', description='Type of custom context variable.'
    )


class CustomContextVariable2(IssueContextVariable):
    field_type: Literal['issue'] = Field(
        ..., alias='@type', description='Type of custom context variable.'
    )


class CustomContextVariable(
    RootModel[Union[CustomContextVariable1, CustomContextVariable2]]
):
    root: Union[CustomContextVariable1, CustomContextVariable2] = Field(
        ..., discriminator='field_type'
    )
