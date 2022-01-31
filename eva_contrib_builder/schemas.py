from typing import List, Optional
from pydantic import BaseModel, Extra
from pydantic.networks import HttpUrl


class Author(BaseModel):
    display_name: str
    url: Optional[HttpUrl]


class BOMItem(BaseModel):
    name: str
    qty: int
    is_printable: bool
    url: Optional[str]


class EasyPageMeta(BaseModel):
    author: Author
    description: str
    bom: List[BOMItem]
    eva_version: str
    print_instructions: str
    step_files: Optional[str]

    class Config:
        extra = Extra.allow
