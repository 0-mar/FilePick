"""Napiš program, který spočítá četnost všech znaků ze zadaného stringu"""


def cetnost_znaku(ret):
    cetnosti = {}
    for znak in ret:
        if znak in cetnosti:
            cetnosti[znak] += 1
        else:
            cetnosti[znak] = 1

    for klic, hodnota in cetnosti.items():
        print(f"Znak {klic}: {hodnota}x")


cetnost_znaku('google.com')