from typing import Dict

import attr

from app.core.dynamic_string import DynamicStringData
from app.core.step_types import StepType
from app.data import BaseEntity


@attr.s(auto_attribs=True)
class HttpStepEntity(BaseEntity):
    http_url: str
    http_method: str
    http_headers: Dict[str, DynamicStringData] = {}
    http_query_params: Dict[str, DynamicStringData] = {}
    http_form_params: Dict[str, DynamicStringData] = {}
    http_request_body: str = ""


@attr.s(auto_attribs=True)
class SqlStepEntity(BaseEntity):
    sql_query: str


def default_step_data(step_type):
    if step_type == StepType.HTTP:
        return HttpStepEntity(http_url="https://httpbin.org/get", http_method="GET")
    elif step_type == StepType.SQL:
        return SqlStepEntity(sql_query="SELECT * FROM World")
