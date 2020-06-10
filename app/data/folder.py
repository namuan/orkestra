from typing import List
from uuid import uuid4

import attr

from app.data import BaseEntity, BaseStore


@attr.s(auto_attribs=True)
class Folder:
    name: str
    selected: bool = False
    id: str = uuid4()


@attr.s(auto_attribs=True)
class FoldersEntity(BaseEntity):
    folders: List[Folder] = [Folder(name="Default")]

# @todo: Add Record Type

class FolderStore(BaseStore):
    def __init__(self, data_store):
        super().__init__(data_store)
        self._folders = FoldersEntity()

    @property
    def folders(self):
        return self._folders
