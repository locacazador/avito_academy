# -*- coding: utf-8 -*-
import json
from typing import Dict, Union, List, Any, Tuple


class Advert:

    def __init__(self, mapping: Dict[str, Union[Dict, str]]):
        self.mapping = mapping

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __getattr__(self, item):
        if not self.mapping.get(item, 0):
            return self.find_recursive_in_dict(
                [(key, value) for key, value in self.__dict__
                 if isinstance(value, dict)],
                item
            )
        self.__setattr__(item, self.mapping[item])
        return self.__dict__.get(item)

    def find_recursive_in_dict(self, list_of_nested_keys: List[Tuple[str, dict]], item: str):
        for attr, value in list_of_nested_keys:
            if isinstance(value, dict):
                self.find_recursive_in_dict()

    def __setattr__(self, key, value):
        self.__dict__[key] = value


class JsonParser:
    def __init__(self, json_object):
        self.raw_data = json_object

    @property
    def python_dict_from_json(self):
        return json.loads(self.raw_data)


if __name__ == '__main__':
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
            }
    }"""
    parser = JsonParser(lesson_str)
    test_1 = Advert(parser.python_dict_from_json)
    print(test_1.location)
