from unittest.mock import patch, MagicMock
import json

import pytest

from what_is_year_now import what_is_year_now

RESPONSE_WITH_HYPHEN = {
    "$id": "1",
    "currentDateTime": "2021-12-01T21:28Z",
    "utcOffset": "00:00:00",
    "isDayLightSavingsTime": False,
    "dayOfTheWeek": "Wednesday",
    "timeZoneName": "UTC",
    "currentFileTime": 132828677340686798,
    "ordinalDate": "2021-335",
    "serviceResponse": None
}

OUTPUT_JSON_WITH_DOT = {
    "$id": "1",
    "currentDateTime": "01.12.2020T21:29Z",
    "utcOffset": "00:00:00",
    "isDayLightSavingsTime": False,
    "dayOfTheWeek": "Wednesday",
    "timeZoneName": "UTC",
    "currentFileTime": 132828677661172303,
    "ordinalDate": "2021-335",
    "serviceResponse": None
}

RESPONSE_WITH_WRONG_DATE_FORMAT = {
    "$id": "1",
    "currentDateTime": "01/12/2020T21:29Z",
    "utcOffset": "00:00:00",
    "isDayLightSavingsTime": False,
    "dayOfTheWeek": "Wednesday",
    "timeZoneName": "UTC",
    "currentFileTime": 132828677661172303,
    "ordinalDate": "2021-335",
    "serviceResponse": None
}


def test_date_with_hyphen():
    """
    Test checks date format contains '-'
    """
    with patch('json.load', return_value=RESPONSE_WITH_HYPHEN):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_date_with_dot():
    """
    Test checks date format contains '.'
    """
    with patch('json.load', return_value=OUTPUT_JSON_WITH_DOT):
        actual = what_is_year_now()
    expected = 2020
    assert actual == expected


def test_wrong_date_format():
    """
    Test checks date format differs from expected
    """
    with patch('json.load', return_value=RESPONSE_WITH_WRONG_DATE_FORMAT):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_no_date_at_all():
    """
    Test checks json format with no date at all
    """
    json.load = MagicMock(return_value={'ML': 'Boosting'})
    with pytest.raises(KeyError):
        what_is_year_now()


def test_date_less_then_four_digits():
    """
    Test checks whether date has str format with len < 4
    """
    json.load = MagicMock(return_value={'currentDateTime': '123'})
    with pytest.raises(IndexError):
        what_is_year_now()
