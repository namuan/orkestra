from enum import Enum

import attr


class DynamicStringType(Enum):
    PLAIN = "plain"
    SECRET = "secret"


@attr.s(auto_attribs=True)
class DynamicStringData(object):
    value: str = ""
    display_text: str = ""
    string_type: str = DynamicStringType.PLAIN.value
    is_enabled: bool = True

    def display_value(self):
        return (
            self.value
            if self.string_type == DynamicStringType.PLAIN.value
            else "*" * len(self.value)
        )
