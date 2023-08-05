"""
Napiš program, který na konzoli vypíše adresářovou strukturu od zadaného adresáře.
Budeme muset použít rekurzi na procházení stromové struktury.

Každá úroveň bude o dvě mezery více vpravo než předchozí.
Pokud program zavoláme na adresář 'rw', dostaneme tento výsledek:

rw
  texty
    recept.txt
    obhajoba.txt
    skola
      jak_podvadet.txt
  fotky
    mnau.png

"""
import sys
from pathlib import Path


def vypis_strom(soubor, odsazeni):
    # TODO veškerý kód přijde sem
    pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Skript musí být spuštěn s 1 argumentem - zdrojovým souborem\n\n"
              "Použití: ./dir_traversal_priklad.py <zdroj>",
              file=sys.stderr)
        exit(1)

    vypis_strom(Path(sys.argv[1]), "")


"""
VOLITELNÉ:
Nyní upravíme program tak, abychom měli ve stromu navíc vodící čárky
│ ├── └──

Pokud program zavoláme na adresář 'rw', dostaneme tento výsledek:

rw
├── texty
│   ├── recept.txt
│   ├── obhajoba.txt
│   └── skola
│       └── jak_podvadet.txt
└── fotky
    └── mnau.png
"""


def vypis_strom2(soubor, odsazeni):
    # TODO veškerý kód přijde sem
    pass


"""if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Skript musí být spuštěn s 1 argumentem - zdrojovým souborem\n\n"
              "Použití: ./dir_traversal_priklad.py <zdroj>",
              file=sys.stderr)
        exit(1)

    vypis_strom2(Path(sys.argv[1]), "")"""