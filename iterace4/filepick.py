#!/usr/bin/python3
"""
Přidáme přepínač -r, který bude určovat, jestli má kopírování proběhnout rekurzivně (pokud bude přítomen).
To znamená že se bude prohledávat celý adresářový strom. Jinak se bude skript chovat jako v 1. iteraci,
tzn. že bude prohledávat soubory jen v našem adresáři.

Dále předělejte skript tak, aby při procházení souborů používal knihovnu pathlib.

Bude se hodit funkce adresar.iterdir() - ta vrati vsechny polozky v danem adresari
soubor.stat().st_ctime - vraci datum vytvoreni
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime


def parse_args():
    pass


def copy_files(source_dir: Path, dest_dir: Path, file_exts, date, recursive):
    pass


def filepick():
    src, dest, file_exts, date, recursive = parse_args()
    copy_files() # TODO spravne zavolej funkci


if __name__ == '__main__':
    filepick()
