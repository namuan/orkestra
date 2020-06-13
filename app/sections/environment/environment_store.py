import logging
from typing import List

import attr

from app.data import BaseStore, BaseEntity

ENVIRONMENT_RECORD_TYPE = "environments"


@attr.s(auto_attribs=True)
class Environment:
    name: str


@attr.s(auto_attribs=True)
class EnvironmentEntity(BaseEntity):
    environments: List[str]
    record_type: str = ENVIRONMENT_RECORD_TYPE


class EnvironmentStore(BaseStore):
    def __init__(self, data_store):
        super().__init__(data_store)

    def upsert_environments(self, environments):
        environment_entity = EnvironmentEntity(
            environments=environments
        )
        table = self.ds.table_for(environment_entity.record_type)
        table.upsert(
            dict(
                name=ENVIRONMENT_RECORD_TYPE,
                object=environment_entity.to_json_str(),
            ),
            ["name"],
        )
        logging.info("Upsert All Environments")
        self.ds.events.environments_added.emit()

    def get_environments(self):
        table = self.ds.table_for(ENVIRONMENT_RECORD_TYPE)
        environments_db = table.find_one(name=ENVIRONMENT_RECORD_TYPE)
        if not environments_db:
            return []

        environment_entity = EnvironmentEntity.from_json_str(environments_db["object"])
        return environment_entity.environments

    def clear_environments(self):
        table = self.ds.table_for(ENVIRONMENT_RECORD_TYPE)
        table.delete(name=ENVIRONMENT_RECORD_TYPE)
