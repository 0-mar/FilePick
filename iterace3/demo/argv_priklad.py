#!/usr/bin/python3

"""
Napiš program, který bude brát 4 povinné poziční argumenty - oddělovač, rok, měsíc a den.
Tyto 4 argumenty následuje libovolné množství názvů souborů.
Pomocí roku, měsíce a dne vytvoříme datetime objekt a vypíšeme datum ve tvaru: <den>[oddělovač]<měsíc>[oddělovač]<rok>
Následovat bude název každého ze souborů na novém řádku.

Dále může program dostat nepovinný přepínač -t. Po něm musí následovat 3 argumenty - hodina, minuty a sekundy.
Pokud program dostane tyto nepovinné hodnoty na vstupu, bude výpis data vypadat takto:

<den>[oddělovač]<měsíc>[oddělovač]<rok> <hodina>[oddělovač]<minuty>[oddělovač]<sekundy>

Pomocí výjimek ošetři všechny neplatné situace tak, aby program vypsal chybové hlášení a skončil s nenulovým
návratovým kódem.
-   nedostatečný počet povinných argumentů
-   špatně zadané časové hodnoty

příklad:
pro volání

./argv_priklad.py . 2023 8 4 neco.txt -t 22 22 0 ahoj.docx bruh.exe

bude výstup:

04.08.2023 22.22.00
neco.txt
ahoj.docx
bruh.exe
"""

from datetime import datetime
import sys


