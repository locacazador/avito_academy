import datetime
import sys
from typing import Callable


def timed_output(function: Callable) -> Callable:
    """
    Add technical information of the current time into stdout
    :param function: function to decorate
    """
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        formatted_now = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}]: "
        sys.stdout.write(formatted_now)
        return function(*args, **kwargs)

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
