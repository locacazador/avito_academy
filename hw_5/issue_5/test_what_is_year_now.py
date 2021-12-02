from unittest.mock import patch, MagicMock
import urllib.request
import io

import pytest

from what_is_year_now import what_is_year_now


def test_date_with_hyphen():
    """
    Test checks date format contains '-'
    """
    date = io.StringIO('{"currentDateTime": "2021-12-01T21:28Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_date_with_dot():
    """
    Test checks date format contains '.'
    """
    date = io.StringIO('{"currentDateTime": "01.12.2020T21:29Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
    expected = 2020
    assert actual == expected


def test_wrong_date_format():
    """
    Test checks date format differs from expected
    """
    date = io.StringIO('{"currentDateTime": "01/12/2020T21:29Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_no_date_at_all():
    """
    Test checks json format with no date at all
    """
    no_date = io.StringIO('{"ML": "Boosting"}')
    urllib.request.urlopen = MagicMock(return_value=no_date)
    with pytest.raises(KeyError):
        what_is_year_now()


def test_date_less_then_four_digits():
    """
    Test checks whether date has str format with len < 4
    """
    date_less_four_digit = io.StringIO('{"currentDateTime": "123"}')
    urllib.request.urlopen = MagicMock(return_value=date_less_four_digit)
    with pytest.raises(IndexError):
        what_is_year_now()
