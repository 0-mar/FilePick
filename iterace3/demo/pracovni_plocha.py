import os

zdroj = os.path.join('rw', 'texty', 'recept.txt')
cil = os.path.join('rw', 'texty', 'vysledek.txt')

with open(zdroj, 'r') as zdroj_soubor, open(cil, 'w') as cil_soubor:
    for line in zdroj_soubor:
        cil_soubor.write(line)