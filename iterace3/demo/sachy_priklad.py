"""
Napiš program, který na základě souřadnic vykreslí momentální stav šachovnice do souboru sachovnice.txt.

Tahy budou ve vstupním souboru odděleny středníkem a budou na jednom řádku
(viz soubor tahy.txt).

První symbol značí figurku, písmeno a číslo je souřadnice políčka.

Pro vstup ze souboru tahy.txt by výsledek měl vypadat takto:

+---+---+---+---+---+---+---+---+
| ♜ |   |   |   |   |   |   |   | 8
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 7
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   | ♕ | 6
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 5
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 4
+---+---+---+---+---+---+---+---+
|   |   | ♙ |   |   |   |   |   | 3
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 2
+---+---+---+---+---+---+---+---+
| ♔ |   |   |   |   |   |   | ♞ | 1
+---+---+---+---+---+---+---+---+
  a   b   c   d   e   f   g   h

"""


import os



