import sys


def redirect_output(filepath):
    def wrapper(function):
        def decorated(*args, **kwargs):
            old_sys_stdout = sys.stdout
            with open(filepath, 'w+') as file_output:
                sys.stdout = file_output
                function(*args, **kwargs)
            sys.stdout = old_sys_stdout
        return decorated
    return wrapper


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


def main():
    calculate()


if __name__ == '__main__':
    main()
