"""
Pro procházení adresářů budeme potřebovat knihovnu os, která obsahuje různé
služby poskytované OS, jako je například vylistování všech položek
adresáře.

Pro kopírování souborů tu pak máme knihovnu shutil.
"""
import os
import shutil

# Nefunguje na Windows kvuli oddelovaci cesty.
# cesta = 'rw/texty'

# Proto je lepší použít funkci os.path.join(), která
# nám pospojuje cestu pomocí oddělovače podle platformy,
# na které momentálně jsme

cesta = os.path.join("rw", "texty")

for soubor in os.listdir(cesta):
    print(soubor)


# zkopiruj soubor obhajoba.txt do skola
zdroj = os.path.join("rw", "texty", "obhajoba.txt")
cil = os.path.join("rw", "skola", "obhajoba.txt")

shutil.copyfile(zdroj, cil)
