"""
Program upravíme tak, aby se k 1 jménu ještě dal uložit email a poznámka.

Po zadání jména nás program vyzve, abychom zadali všechny ostatní informace
ve formátu <cislo>;<email>;<poznamka>. Email a poznámka však nejsou povinné.

Jméno bude opět klíč a jako hodnota nám poslouží ntice, která se skládá ze
všech informací o člověku.

příklad: {Karel Vomáčka: ("787 784 954", "kv@gmail.com", "dluzi mi za kebab")}
"""

kontakty = {}   # alternativne take kontakty = dict()

def fce():
    while True:
        jmeno = input("Zadej jmeno nebo konec: ")
        if jmeno == "konec":
            break
        else:
            data = input("Zadej ostatni informace: ")
            rozdelene = tuple(data.split(";"))
            kontakty[jmeno] = rozdelene


    print(kontakty)


fce()

ntice = ("fdsfds", 5, "xdd")
kontakty["jan"] = ntice
seznam = "fd;as;fa;sd".split(";")

tuple([0, 1, 2, 3, 4])
kontakty["jan"] = seznam
