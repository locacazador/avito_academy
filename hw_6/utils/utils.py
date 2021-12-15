

def my_write(string_text):
    if not string_text.rstrip():  # \n
        return string_text.rstrip()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_now = f"[{now}]: {string_text}\n"
    original_write(formatted_now)
