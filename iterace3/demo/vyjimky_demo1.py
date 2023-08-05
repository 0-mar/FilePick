"""
Výjimky jsou velice efektivní a účinný způsob jak řešit nenadálé situace v programu, kdy se stalo
něco mimořádného (což je většinou chyba). Například jsme ve funkci chtěli číslo, ale místo toho
jsme dostali string.

V takové situaci chceme mít nějaký způsob, kterým můžeme signalizovat tuhle chybovou situaci.
Výjimku si můžeme představit jako takovou notifikaci, která je vyvolaná, pokud taková situace nastane.
Jako programátor pak můžeme na tuhle notifikaci nějakým způsobem zareagovat - často všechno zapálit
a shodit, protože pokud náš program spoléhá na práci s nějakým souborem a ten neexistuje, tak jsme
takzvaně v řiti a nemá smysl pokračovat.
"""


def deleni_nulou():
    return 5 / 0


# pokud je výjimka neošetřena, shodí nám okamžitě program
# to ale není vždycky dobré chování
deleni_nulou()


# potenciálně promblatickou část obalíme do try bloku
# pokud uvnitř nastane výjimka, tak může být ošetřena jedním z except bloků
try:
    deleni_nulou()

# tento blok ošetřuje dělení nulou
except ZeroDivisionError as err:
    print("deleni nulou, ale nekoncim")
    # zpráva o vyvolané výjimce
    print(err.args)
