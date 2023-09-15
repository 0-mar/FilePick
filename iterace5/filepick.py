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
    pass


def copy_files(source_dir: Path, dest_dir: Path, file_exts, date, recursive):
    pass


def filepick():
    src, dest, file_exts, date, recursive = parse_args()
    copy_files()  # TODO spravne zavolej funkci


if __name__ == '__main__':
    filepick()
