#!/usr/bin/python3

"""
Skript upravíme tak, aby nyní vykopíroval všechny vyhovující soubory,
které se nachází kdekoliv v adresářovém podstromu.

Ke zjištění, zda je nalezná položka soubor nebo adresář,
použijeme funkce

os.path.isfile(cesta) a os.path.isdir(cesta)
"""

import os
import sys
import shutil

FILE_EXTS = ('.docx', '.txt')


def filepick():
    # TODO veškerý kód přijde sem
    pass


if __name__ == '__main__':
    filepick()
