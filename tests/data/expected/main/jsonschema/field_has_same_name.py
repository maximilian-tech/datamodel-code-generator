# generated by datamodel-codegen:
#   filename:  field_has_same_name.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class TestObject(BaseModel):
    test_string: Optional[str] = None


class Test(BaseModel):
    TestObject: Optional[TestObject] = Field(None, title='TestObject')
