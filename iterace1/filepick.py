#!/usr/bin/python3
"""
Napiš skript, který zkopíruje ze zdrojového adresáře do cílového jen ty soubory,
které mají koncovku obsaženou v FILE_EXTS.

Zdrojový a cílový adresář program dostane na příkazové řádce.

V případě, že bylo zadáno málo argumentů na příkazovou řádku, by
skript měl skončit s chybovou hláškou a nenulovým návratovým kódem.

Toho docílíme pomocí klasického printu, jenom přidáme volitelný argument file
print("Vypiš na stderr.", file=sys.stderr)
Násilné ukončení programu s nenulovým návratovým kódem provedeme pomocí funkce
exit(1)
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
