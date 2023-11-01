slovnik = {"resolution": "1920x1200", "shaders": True, "texture_quality": "high", "max_fps": 120}

"""
Když dáme slovník do cyklu for, dostaneme klíče (keys)
"""
"""for key in slovnik:
    print(key)"""


"""
Pokud chceme hodnoty (values), stačí použít metodu values.
"""

"""for value in slovnik.values():
    print(value)"""


"""
Často jsou ale potřeba jak klíče, tak hodnoty. K tomu mají slovníky metodu items(),
která bude v cyklu for dávat dvojice (ntici se 2 prvky)
"""
for key, value in slovnik.items():
    print(f"{key}: {value}")
    print(str(key) + ": " + str(value))