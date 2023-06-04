def italic(s: str) -> str:
    s = s.replace('*', '<em>', 1)
    reversed_string = s[::-1]
    reversed_string = reversed_string.replace('*', '</em>'[::-1], 1)
    return reversed_string[::-1]


def bold(s: str) -> str:
    s = s.replace('**', '<strong>', 1)
    reversed_string = s[::-1]
    reversed_string = reversed_string.replace('**', '</strong>'[::-1], 1)
    return reversed_string[::-1]


if __name__ == "__main__":
    txt = input('Введите Markdown-строку для форматирования\n')
    if txt[0] == '*' and txt[-1] == '*':
        if txt[1] == '*' and txt[-2] == '*':
            txt = bold(txt)
        else:
            txt = italic(txt)
    print('Отформатированная строка:\n' + txt)
