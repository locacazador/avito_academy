import json
from typing import Dict, Union
from keyword import iskeyword


class ColorizeMixIn:
    """Class to colorize output in stdout"""

    def __init__(self, repr_color_code):
        self.repr_color_code = repr_color_code

    def __str__(self):
        """
        Colorize stdout

        :return: colorized string if color code is set
        """

        print_text = self.__repr__()
        return f'\033[0;{self.repr_color_code}m' + print_text


class Advert(ColorizeMixIn):
    """Class to interact with json attributes"""

    def __init__(self, mapping: Dict[Union[str, dict, int],
                                     Union[str, dict, int]],
                 repr_color_code=0):
        super().__init__(repr_color_code)
        mapper = InnerNestedAttribute(mapping).__dict__
        if mapper.get('price', 0) < 0:
            raise ValueError('price must be >= 0')
        self.__dict__.update(InnerNestedAttribute(mapping).__dict__)

    def __getattr__(self, item):
        """
        :raise ValueError if no such attribute in json
        :param item: item not from attributes
        """

        raise ValueError('No such attribute in json object')

    def __repr__(self) -> str:
        """
        Provide string with title & price of the json object

        :return: title & price
        """

        return f'{self.title} | {self.price} ₽'

    @property
    def price(self) -> Union[int, int]:
        """
        Price getter

        :return: 0 if no price else price
        """

        return self.__dict__.get('price', 0)

    @price.setter
    def price(self, set_price):
        if set_price < 0:
            raise ValueError('price must be >= 0')


class InnerNestedAttribute:
    """Class to perform nested dict attribute in parsed json"""

    def __init__(self, data_dict: Dict[Union[str, dict, int],
                                       Union[str, dict, int]]):
        for key, value in data_dict.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = InnerNestedAttribute(value)
            else:
                self.__dict__[key] = value

    def __str__(self):
        return f'{self.__dict__}'


if __name__ == '__main__':
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
            }
    }"""
    parsed_dict_data = json.loads(lesson_str)
    test_1 = Advert(parsed_dict_data)
    print(test_1.location.address)
    print(test_1.location)
    corgi = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, Тишково, 25"
        }
    }
    """
    test_2 = Advert(json.loads(corgi))
    print(test_2.class_)
    price_zero_value = '{"title": "python"}'
    test_3 = Advert(json.loads(price_zero_value))
    print(test_3.price)
    price_less_zero_value = '{"title": "python", "price": -2}'
    try:
        test_4 = Advert(json.loads(price_less_zero_value))
    except ValueError as e:
        print(str(e))
    try:
        test_3.price = -20
    except ValueError as e:
        print(str(e))
    iphone_X = """{
    "title": "iPhone X",
    "price": 100,
    "location": {
    "address": "город Самара, улица Мориса Тореза, 50",
    "metro_stations": ["Спортивная", "Гагаринская"]
            }
    }"""
    test_5 = Advert(json.loads(iphone_X))
    print(test_5)
    test_6 = Advert(json.loads(corgi), repr_color_code=32)
    print(test_6)
