slovnik = {"resolution": "1920x1200", "shaders": True, "texture_quality": "high", "max_fps": 120}
"""
Slovník se dá vytvořit dvěma způsoby. Buď pomocí složených závorek,
nebo funkce dict(). Ta, stejně jako str, int či list, převede cokoli, co jde, na slovník.

Také díky ní můžeme vytvořit prázdný slovník
"""

prazdny = dict()
print(prazdny)

# funkci dict muzeme predat bud jiny slovnik, cimz vytvorime kopii
kopie = dict(slovnik)
print(kopie)

# muzeme ji take predat data ve forme dvojic klic/hodnota
data = [("a", 1), ("b", 2), ("c", 3)]
s = dict(data)
print(s)
