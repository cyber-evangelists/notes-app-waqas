from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime


T = TypeVar("T")


class NotesSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    check_in: Optional[bool] = False
    # profile_photo: Optional[bytes] = None
    created_at: datetime
    # image: Optional[bytes] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
       
       
class ClientDataSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    access_token: Optional[str] = None


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestNotes(BaseModel):
    parameter: NotesSchema = Field(...)
    

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
