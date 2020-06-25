import attr

from app.core.step_types import StepType
from app.data import BaseEntity


@attr.s(auto_attribs=True)
class HttpStepEntity(BaseEntity):
    http_url: str
    http_method: str


@attr.s(auto_attribs=True)
class SqlStepEntity(BaseEntity):
    sql_query: str


def default_step_data(step_type):
    if step_type == StepType.HTTP:
        return HttpStepEntity(http_url="https://httpbin.org/get", http_method="GET")
    elif step_type == StepType.SQL:
        return SqlStepEntity(sql_query="SELECT * FROM World")
