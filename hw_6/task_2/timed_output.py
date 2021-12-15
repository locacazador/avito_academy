import datetime
import sys
from typing import Callable


def timed_output(function: Callable) -> Callable:
    """
    Add technical information of the current time into stdout
    :param function: function to decorate
    """

    def wrapper(*args, **kwargs) -> Callable:
        original_write = sys.stdout.write

        def my_write(string_text):
            if not string_text.rstrip():  # \n
                return string_text.rstrip()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            formatted_now = f"[{now}]: {string_text}\n"
            original_write(formatted_now)

        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name: str):
    """
    Print greeting with technical info
    :param name: name of the user. Expects string
    """
    print(f'Hello, {name}!')


def main():
    print_greeting(input('Enter your name!\n'))


if __name__ == '__main__':
    main()
