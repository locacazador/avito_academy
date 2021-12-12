import datetime
import sys
from unittest.mock import patch
from io import StringIO

from timed_output import print_greeting


def test_timed_print():
    """
    Test  print_greeting function with decorator @timed_output
    """
    current_time = datetime.datetime(year=2021, month=12, day=5,
                                     hour=12, minute=0, second=0)
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = current_time
            with patch('builtins.input', return_value='Volodya'):
                print_greeting(input())
                assert mock_stdout.getvalue() == '[2021-12-05 12:00:00]: Hello, Volodya!\n'
