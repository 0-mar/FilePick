"""
Pro práci s argumenty z příkazové řádky použijeme modul sys. Ten obsahuje věci spojené s interpreterem, mimo jiné
i právě argumenty z příkazové řádky.
"""

import sys

print(sys.argv)

# první argument je vždy název skriptu:
print(sys.argv[0])
print()

# přes argumenty můžeme klasicky iterovat nebo si zjistit jejich počet, protože
# se jedná o klasické pole
for arg in sys.argv:
    print(arg)

