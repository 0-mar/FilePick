"""
Čtení a zapisování do souborů
https://realpython.com/read-write-files-python/

"""

# Nefunguje na Windows kvuli oddelovaci cesty.
# pro multiplatformni kod lepsi pouzit:
# os.path.join('rw', 'texty', 'recept.txt')
soubor = open('rw/texty/recept.txt')

# moznost cislo 1, vzdy je potreba soubor zavrit!
try:
    # sem prijde prace se souborem
    radek = soubor.readline()
    while radek != "":  # dokud neni EOF
        print(radek, end="")
        radek = soubor.readline()

finally:
    # nutne zavrit soubor!
    soubor.close()

# moznost 2, diky context manageru nemusime resit zavirani manualne
with open('rw/texty/recept.txt') as soubor:
    for radek in soubor.readlines():
        print(radek, end="")


# zápis do souboru:
with open("rw/texty/test.txt", 'w') as soubor:
    soubor.write("aaaaaaaaa")
    soubor.write("bb")


# Existuje několik režimů, ve kterých se dají soubory otevírat. Nejzajímavější je asi rozdíl mezi textovým vs
# binárním režimem. V textovém režimu se bajty nejprve dekódují podle daného formátu (defaulutně je to UTF-8).
# V binárním režimu dostáváme zpět surové bajty bez jakéhokoliv předzpracování. Rozdíl bychom poznali na diakritice
# nebo CR LF.
"""
Mode	Description
-------------------
t	    Open in text mode. (default)
b	    Open in binary mode.

r	    Open a file for reading. (default)
w	    Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	    Open a file for exclusive creation. If the file already exists, the operation fails.
a	    Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
+	    Open a file for updating (reading and writing)
"""

# čtení v binárním režimu:
with open("rw/texty/recept.txt", 'rb') as soubor:
    print(soubor.readline())

# Jeden bajt nabývá hodnot v rozsahu 0 až 255. Každé hodnotě je přiřazen v ASCII nějaký znak. Při výpisu
# se nám nezobrazují jednotlivé hodnoty bajtů, ale jejich odpovídající znak v ASCII (pokud se nejedná o nějaký
# zvláštní netisknutelný znak, pak dostáváme hodnotu bajtu v šestnáctkové soustavě).

# Binární režim je užitečný, pokud potřebujeme zpracovat třeba fotku v PNG formátu a potřebujeme jednotlivé bajty.
