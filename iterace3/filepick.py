#!/usr/bin/python3
"""
Skript upravíme tak, aby nyní šlo vybírat, jaký typ souborů budeme kopírovat (přípony).
Kromě toho také přidáme možnost specifikace data. Zkopírují se pouze ty soubory, které
jsou novější nebo stejně staré (rozhodujeme podle data vytvoření souboru) jako námi
zadané datum. Pokud datum nezadáme, automaticky se použije to dnešní
(tzn. zkopírují se jen dnešní soubory).

Datum vytvoření souboru zjistíme pomocí této funkce:
os.path.getctime(filepath)
která bere jako parametr cestu k danému souboru.

Kromě toho také ošetřete následující chyby:
 - zdrojový adresář neexistuje
 - zdroj není adresář
 - po přepínači -d nenásleduje validní datum
   (můžete zvolit např. formát DD/MM/RRRR)

Pokud nastane jakákoliv chyba, program skončí s chybovou hláškovou
na stderr a nenulovým návratovým kódem.

Doporučuju si vytvořit separátní funkci pro parsování argumentů z příkazové řádky.

Skript se spouští následovně: ./filepick.py <zdroj> <destinace> [-d datum] [seznam přípon]
"""

import os
import sys
import shutil
from datetime import datetime


def parse_args():
    """
    Zpracuje argumenty z příkazové řádky.

    :return: Vrací cestu k zdrojovému adresáři, cílovému adresáři, seznam chtěných přípon a filtrovací datum.
    """

    return "", "", [], None


def filepick():
    src, dest, file_exts, date = parse_args()
    # TODO zbytek kódu


if __name__ == '__main__':
    filepick()
