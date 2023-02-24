import logging
from typing import List, Dict, Optional

import attr

from app.data import BaseStore, BaseEntity

ENVIRONMENT_RECORD_TYPE = "environments"


@attr.s(auto_attribs=True)
class Environment:
    name: str
    variables: Optional[Dict] = {}


@attr.s(auto_attribs=True)
class EnvironmentEntity(BaseEntity):
    environments: List[Environment]
    record_type: str = ENVIRONMENT_RECORD_TYPE


class EnvironmentStore(BaseStore):
    def __init__(self, data_store):
        super().__init__(data_store)

    def upsert_environments(self, environments):
        environment_entity = EnvironmentEntity(
            environments=[
                Environment(name=k, variables=v) for k, v in environments.items()
            ]
        )
        table = self.ds.table_for(environment_entity.record_type)
        table.upsert(
            dict(
                name=ENVIRONMENT_RECORD_TYPE,
                object=environment_entity.to_json_str(),
            ),
            ["name"],
        )
        logging.info("Upsert All Environments - Total: {}".format(len(environments)))
        self.ds.events.environments_changed.emit()

    def get_environments(self):
        table = self.ds.table_for(ENVIRONMENT_RECORD_TYPE)
        environments_db = table.find_one(name=ENVIRONMENT_RECORD_TYPE)
        if not environments_db:
            return []

        environment_entity = EnvironmentEntity.from_json_str(environments_db["object"])
        return environment_entity.environments

    def get_environment(self, environment_name):
        environments = self.get_environments()
        return next((e for e in environments if e.name == environment_name), None)

    def clear_environments(self):
        table = self.ds.table_for(ENVIRONMENT_RECORD_TYPE)
        table.delete(name=ENVIRONMENT_RECORD_TYPE)
