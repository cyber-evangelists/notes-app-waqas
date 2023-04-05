# from typing import List, Optional, Generic, TypeVar
# from pydantic import BaseModel, Field
# from pydantic.generics import GenericModel

# T = TypeVar("T")


# class YtLinkSchema(BaseModel):
#     id = Optional[int] = None
#     title = Optional[str] = None
#     description = Optional[str] = None
#     link = Optional[str] = None

#     class Config:
#         orm_mode = True


# class RequestYtLink(BaseModel):
#     parameter: YtLinkSchema = Field(...)


# class Response(GenericModel, Generic[T]):
#     code: str
#     status: str
#     message: str
#     result: Optional[T]

