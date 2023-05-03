from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime


T = TypeVar("T")


class NotesSchema(BaseModel):
    id: int = None
    title: Optional[str] = None
    description: Optional[str] = None
    check_in: Optional[bool] = False
    # image : Optional[bytes] = None
    created_at: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ClientDataSchema(BaseModel):
    access_token: str = None


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestNotes(BaseModel):
    parameter: NotesSchema = Field(...)


class RequestClientData(BaseModel):
    parameter: ClientDataSchema = Field(...)


class Response(GenericModel, Generic[T]):
    message: Optional[str]
    result: Optional[T]


class NotesResponse(BaseModel):
    id: Optional[int]


class ClientDataResponse(BaseModel):
    id: Optional[int]
    name: Optional[str]
    email: Optional[str]
