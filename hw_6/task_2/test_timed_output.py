from unittest.mock import patch
from io import StringIO

import timed_output


def test_timed_print():
    """
    Test print_greeting function with decorator @timed_output
    """
    current_time = timed_output.datetime.datetime(year=2021, month=12, day=5,
                                                  hour=12, minute=0, second=0)
    with patch('sys.stdout', new=StringIO()) as mock_stdout, \
            patch('timed_output.datetime.datetime') as mock_date, \
            patch('builtins.input', return_value='Volodya'):
        mock_date.now.return_value = current_time
        timed_output.print_greeting(input())
        assert mock_stdout.getvalue() == '[2021-12-05 12:00:00]:' \
                                         ' Hello, Volodya!\n'
