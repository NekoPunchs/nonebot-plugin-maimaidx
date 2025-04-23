import os.path
import re
from pathlib import Path

import regex


def read_all_text(path: Path) -> str:
    if not os.path.exists(path):
        return ''
    with open(path, mode='r', encoding='utf-8') as c:
        return c.read()


def read_all_lines(path: Path, split: str = '\n') -> list[str]:
    t = read_all_text(path)
    if t is None:
        return list[str]()
    a = t.split(split)
    return a


def write_all_txt(path: Path, value: str, append: bool):
    if append:
        mode = 'a'
    else:
        mode = 'w'

    with open(path, mode=mode, encoding='utf-8') as c:
        c.write(value)


def get_files(path: Path, ext: str) -> list[str]:
    result = list[str]()

    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(ext):
                continue
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                result.append(file_path)
    return result
