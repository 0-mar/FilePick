#!/usr/bin/python3
"""
Upravíme skript tak, aby používal knihovnu argparse. To je velice užitečná knihovna, která slouží
k vytvoření rozhraní programu z příkazové řádky.

Dojde k jedné změně - koncovky souborů se budou zadávat po přepínači -e, který je volitelný.
Defaulutní zůstanou .txt a .docx.

Příklad použití:
./filepick.py <zdroj> <destinace> [-d datum] [-e seznam přípon] [-r]

Potřebné info zkuste najít tady:
https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args
"""


import shutil
from pathlib import Path
from datetime import datetime
import argparse


def parse_args():
    parser = argparse.ArgumentParser(prog='FilePick')
    parser.add_argument("source")
    parser.add_argument("destination")
    parser.add_argument('-r', '--recursive', action='store_true')
    parser.add_argument('-d', '--date', default=datetime.now().date().strftime("%d/%m/%Y"))
    parser.add_argument('-e', '--extensions', nargs="*", default=[".txt", ".docx"])

    args = parser.parse_args()

    return args.source, args.destination, args.extensions, datetime.strptime(args.date, "%d/%m/%Y"), args.recursive


def copy_files(source_dir: Path, dest_dir: Path, file_exts, date, recursive):
    for file in source_dir.iterdir():
        creation_date = file.stat().st_ctime
        if file.is_file() and file.name.endswith(tuple(file_exts)) and creation_date >= date:
            shutil.copyfile(file, Path(dest_dir, file.name))
        elif file.is_dir() and recursive:
            copy_files(file, dest_dir, file_exts, date, recursive)


def filepick():
    src, dest, file_exts, date, recursive = parse_args()
    copy_files(Path(src), Path(dest), file_exts, date.timestamp(), recursive)


if __name__ == '__main__':
    filepick()
