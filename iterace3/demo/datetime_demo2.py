"""
datetime = modul ve standardní knihovně Pythonu pro manipulaci s datem a časem.
Modul obsahuje několik tříd, z nichž nejzajímavější pro nás bude datetime, který kombinuje
datum a čas. Abychom s ní mohli pracovat, musíme jí nejdříve naimportovat:
"""

from datetime import datetime

# vytvoření instance s datumem 21.7.2064
datum = datetime(2064, 7, 21)
print(datum)

# můžeme dokonce přidat hodiny, minuty a sekundy
datum = datetime(2064, 7, 21, 8, 5, 15)
print(datum)
# datum.replace(hour=8, minute=5, second=15)

# funkcí now() dostaneme momentální datum a čas:
datum = datetime.now()
print(datum)

# funkcí strftime vypíšeme datum v námi zvoleném formátu
print(datum.strftime("Dnes je %A %d.%m.%Y"))

# funkcí strptime naparsujeme a vytvoříme instanci datetime ze stringu, jehož formát musíme znát
# toto je užitečné především pokud chceme nějak zpracovat uživatelem zadané datum a čas
date_str = '18.11.2008'
datum = datetime.strptime(date_str, '%d.%m.%Y')
print(datum)

# velice užitečná funkce je timestamp(), která vrací tzv. časové razítko = počet sekund od 1.1.1970
print(datum.timestamp())


