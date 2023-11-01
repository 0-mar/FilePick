"""
Napiš program, který bude fungovat jako správce kontaktů.

Zeptá se na jméno a pro něj uloží telefonní číslo, které zadá uživatel.
"""

kontakty = {}   # alternativne take kontakty = dict()

def fce():
    while True:
        jmeno = input("Zadej jmeno nebo konec: ")
        if jmeno == "konec":
            break
        else:
            cislo = input("Zadej cislo: ")
            kontakty[jmeno] = cislo

    print(kontakty)


fce()