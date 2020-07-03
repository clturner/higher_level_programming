#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    dic = { "  ": "", "   ": "", "    ": " ", "..": ".", "...": ".", "....": "." }
    for name, value in dic.items():
        text = text.replace(name, value)
    dic = { ".": ".\n\n", "?": "?\n\n", ":": ":\n\n" }
    for name, value in dic.items():
        text = text.replace(name, value)
    dic = {".\n\n ": ".\n\n", "?\n\n ": "?\n\n", ":\n\n ": ":\n\n"}
    for name, value in dic.items():
        text = text.replace(name, value)
    print(text, end="")
