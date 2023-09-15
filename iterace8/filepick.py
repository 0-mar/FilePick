#!/usr/bin/python3
import math
import shutil
from pathlib import Path
import datetime
import argparse
from typing import List

"""
Náš backend aplikace filepick musíme trochu poupravit. Místo pouhého 'date' přidáme dva přepínače -fd (fromdate)
a -td (todate), což bude časové rozmezí, které se použije na soubory (soubory, které do něj spadají, se překopírují).
Defaulutní hodnota -fd bude 01/01/0001, -td bude
datetime.date.max.strftime("%d/%m/%Y") (vrátí tuto reprezantaci data pro maximální datum).

Dále přidáme ještě přepínač -a (all), který signalizuje, že máme kopírovat všechny nalezené soubory. Také ještě
upravíme přepínač -e, odteď nebude mít žádnou defaulutní hodnotu.
Přepínač -a bude společně s přepínačem -e ve vzájemně výlučné skupině (tzn. pokud program volám s jedním,
nemůžu ho zavolat i s druhým). Toho dosáhneme pomocí metody parser.add_mutually_exclusive_group(), která vrátí
takovou skupinu. Do ní poté přidáváme argumenty úplně stejným způsobem jako do parseru.

Nakonec musíme program upravit tak, aby reflektoval změny v rozhraní příkazové řádky. Funkce parse_args()
bude stále vracet všechny zparsované možnosti, ale s mírným rozdílem u datumů. Tam chceme vracet pouze uživatelem
zadané datumové stringy. V hlavní funkci filepick() se je totiž pokusíme převést na datetime objekty
pomocí funkce strptime() a rovnou získat timestamp pomocí funkce timestamp(). Při tomto procesu může
být vyhozena ValueError. V takovém případě nastavíme fromdate na 0 a todate na math.inf (nekonečno).

Dále bude potřeba trochu upravit i funkci copy_files() - hlavičku, ale i podmínky a rekurzivní volání funkce. 
"""


def parse_args():
    pass


def copy_files():
    # TODO
    pass


def filepick():
    src, dest, recursive, fromdate, todate, exts, all_files = parse_args()
    copy_files()  # TODO


if __name__ == '__main__':
    filepick()
