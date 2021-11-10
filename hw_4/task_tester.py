from json import loads

from hw_4.advert import Advert


class TaskTester:
    SINGLE_AND_NESTED_ATTR_TEST = """{
                "title": "python",
                "price": 0,
                "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"],
                "class": "dogs"
                        }
                }"""

    def __init__(self):
        self.SINGLE_ATTR = 'python'
        self.NESTED_ATTR = 'location'
        self.NESTED_INNER_ATTR = 'metro_stations'
        self.KEYWORD_ATTR = 'dogs'

    def check_getting_not_nested_attr(self):
        print('Running single attribute test!')
        test_advert = Advert(loads(self.SINGLE_AND_NESTED_ATTR_TEST))
        actual_value = test_advert.title
        if actual_value != self.SINGLE_ATTR:
            print(f'Single attribute test failed!'
                  f' Expected {self.SINGLE_ATTR}, got {actual_value}')
        print('Running nested attribute test!')




