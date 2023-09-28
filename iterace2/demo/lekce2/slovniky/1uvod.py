"""
Další základní datová struktura, kterou si představíme, jsou slovníky (angl. dictionary, dict).

Podobně jako seznamy a ntice v sobě slovníky obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence,
ve slovnících máme dva druhy prvků: takzvaný klíč (key) a hodnotu (value).
Každému klíči je přiřazena právě jedna hodnota.

Slovník můžeš použít, když máš několik kousků informací, které se dají pojmenovat,
ale chceš s nimi pracovat jako s jednou proměnnou.
"""



slovnik = {"resolution": "1920x1200", "shaders": True, "texture_quality": "high", "max_fps": 120}
print(slovnik)


# hodnoty ze slovníku se získávají podobně jako ze seznamu, jen místo indexu
# se použije klíč

print(slovnik["resolution"])

# neexistujicí klíč - vyhodi vyjimku
print(slovnik["neexistuju"])

# hodnoty jdou podle klíče i měnit
slovnik["shaders"] = False
print(slovnik)


# můžu je přidávat tak, že novému klíči přiřadím hodnotu
slovnik["antialiasing"] = False
print(slovnik)


# jednotlivé záznamy je také možné mazat pomocí del
del slovnik["max_fps"]
print(slovnik)



