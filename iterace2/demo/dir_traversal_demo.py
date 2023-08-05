"""
Jak to udělat, pokud chceme procházet adresářový strom od určitého adresáře?

rw/
├── fotky/
│   └── mnau.png
└── texty/
    ├── skola/
    │   └── jak_podvadet.txt
    ├── obhajoba.txt
    └── recept.txt

Tzn. chtěli bychom objevit všechny soubory cats.gif, manu.png, recept.txt atd.
Problém je, že dopředu nikdy nemůžeme vědět, jak bude strom vypadat.

Náš problém vyřešíme pomocí tzv. rekurze.

Budeme chtít vypsat obsah všech textových souborů, které najdeme.
"""

# budeme potřebovat knihovnu os
import os


def vypis_soubor(cesta):
    with open(cesta) as cteni:
        for radek in cteni:
            print(radek, end="")
    print()


def prochazej_adresare(zdrojovy_adr):
    # funkce listdir vrátí seznam všech položek v daném adresáři
    obsah = os.listdir(zdrojovy_adr)
    for soubor in obsah:
        cesta = os.path.join(zdrojovy_adr, soubor)
        # funkce os.path.isfile vrátí True, pokud se jedná o soubor
        if os.path.isfile(cesta) and soubor.endswith(".txt"):
            vypis_soubor(cesta)
        # funkce os.path.isdir vrátí True, pokud se jedná o adresář
        elif os.path.isdir(cesta):
            prochazej_adresare(cesta)


prochazej_adresare("rw")

"""
Knihovna pathlib
"""
# s využitím pathlib
from pathlib import Path


def prochazej_adresare2(zdrojovy_adr):
    for soubor in zdrojovy_adr.iterdir():
        # metoda is_file vrátí True, pokud se jedná o soubor
        if soubor.is_file():
            vypis_soubor(soubor)
        # metoda is_dir vrátí True, pokud se jedná o adresář
        elif soubor.is_dir():
            prochazej_adresare(soubor)


#prochazej_adresare2(Path("rw"))
