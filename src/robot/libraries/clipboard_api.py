import pyperclip


def clipboard_set(text):
    pyperclip.copy(text)


def clipboard_get():
    return pyperclip.paste()
