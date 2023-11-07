# generated by datamodel-codegen:
#   filename:  enum_models.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field


class Kind(Enum):
    dog = 'dog'
    cat = 'cat'


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
    kind: Optional[Kind] = None
    type: Optional[Literal['animal']] = None
    number: Literal[1] = 1
    boolean: Literal[True] = True


class Pets(BaseModel):
    __root__: List[Pet]


class Kind1(Enum):
    snake = 'snake'
    rabbit = 'rabbit'


class Animal(BaseModel):
    kind: Optional[Kind1] = None


class Error(BaseModel):
    code: int
    message: str


class Type(Enum):
    a = 'a'
    b = 'b'


class EnumObject(BaseModel):
    type: Optional[Type] = None


class EnumRoot(Enum):
    a = 'a'
    b = 'b'


class IntEnum(Enum):
    number_1 = 1
    number_2 = 2


class AliasEnum(Enum):
    a = 1
    b = 2
    c = 3


class MultipleTypeEnum(Enum):
    red = 'red'
    amber = 'amber'
    green = 'green'
    NoneType_None = None
    int_42 = 42


class SingleEnum(BaseModel):
    __root__: Literal['pet'] = 'pet'


class ArrayEnum(BaseModel):
    __root__: List[Union[Literal['cat'], Literal['dog']]]


class NestedVersionEnum(Enum):
    RC1 = 'RC1'
    RC1N = 'RC1N'
    RC2 = 'RC2'
    RC2N = 'RC2N'
    RC3 = 'RC3'
    RC4 = 'RC4'


class NestedVersion(BaseModel):
    __root__: Optional[NestedVersionEnum] = Field(
        'RC1', description='nullable enum', example='RC2'
    )


class NestedNullableEnum(BaseModel):
    nested_version: Optional[NestedVersion] = Field(
        default_factory=lambda: NestedVersion.parse_obj('RC1'),
        description='nullable enum',
        example='RC2',
    )


class VersionEnum(Enum):
    RC1 = 'RC1'
    RC1N = 'RC1N'
    RC2 = 'RC2'
    RC2N = 'RC2N'
    RC3 = 'RC3'
    RC4 = 'RC4'


class Version(BaseModel):
    __root__: Optional[VersionEnum] = Field(
        'RC1', description='nullable enum', example='RC2'
    )