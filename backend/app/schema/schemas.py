from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field, EmailStr
from pydantic.generics import GenericModel
from datetime import datetime


T = TypeVar("T")

class NotesSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    check_in: Optional[bool] = False
    # image : Optional[bytes] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ClientDataSchema(BaseModel):
    access_token: str = None
    
    
class MyUserSchema(BaseModel):
    # username: str = Field(..., min_length = 5, max_length = 255)
    email: str = Field(..., max_length = 255)
    password: str = Field(..., min_length = 8)
    
    
class LoginMyUserSchema(BaseModel):
    email: EmailStr = None
    password: str = None


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestNotes(BaseModel):
    parameter: NotesSchema = Field(...)


class RequestClientData(BaseModel):
    parameter: ClientDataSchema = Field(...)
    
    
class RequestMyUser(BaseModel):
    parameter: MyUserSchema = Field(...)


class RequestLoginMyUser(BaseModel):
    parameter: LoginMyUserSchema = Field(...)


class Response(GenericModel, Generic[T]):
    message: Optional[str]
    result: Optional[T]


class NotesResponse(BaseModel):
    id: Optional[int]


class ClientDataResponse(BaseModel):
    name: Optional[str]
    email: Optional[str]
