# from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel
# from pydantic.generics import GenericModel


class CreateNotesRequest(BaseModel):
    id: int
    title: str
    description: str
    url: str
