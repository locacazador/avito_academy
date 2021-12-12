import datetime
import sys


ORIGINAL_WRITE = sys.stdout.write


def my_write(string_text):
    if not len(string_text.rstrip()):  # because standard print method adds \n character
        return
    now = datetime.datetime.now()
    formatted_now = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}]: "
    output_row = formatted_now + string_text + '\n'
    ORIGINAL_WRITE(output_row)


def main():
    sys.stdout.write = my_write  # override write method of sys.stdout
    print(input())  # uses my_write function because of overriding
    sys.stdout.write = ORIGINAL_WRITE  # return original write method


if __name__ == '__main__':
    main()
