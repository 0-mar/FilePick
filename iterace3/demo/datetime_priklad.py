#!/usr/bin/python3

"""
Napiš program, který si vyžádá datum ve tvaru DD.MM.RRRR (např. 2.5.2205).
Text níže potom zašifruj tak, abys k ordinální hodnotě každého znaku přičetl rok a odečetl měsíc * den.

Jedině díky tomuhle programu si zachováš aspoň jednu mozkovou hemisféru po přečtení textu.
"""

from datetime import datetime

text = """Haf! Haf!
Ty takhle štěkáš?
Tak to budeš moje Hafo
Jak jako Hafo?
Moje holka je nějaká divná
Má na sobě obojek a chodí po čtyrech
A ukazuje ass, já slintám jak pes
Hafo hafo hafo, chci jí mít nahoře bez (pojď, pojď)
Baby ty jseš Hafo, baby chci tě hafo
Baby ty jseš Hafo, baby tak pojď na to
Ukazuje ass, já slintám jak pes
Hafo hafo hafo, chci jí mít nahoře bez (pojď, pojď, pojď)
Baby ty jseš Hafo, baby chci tě hafo
Baby ty jseš Hafo, baby tak pojď na to
Ukazuje ass, já slintám jak pes
Hafo hafo hafo, chci jí mít nahoře bez (pojď, pojď, pojď)
Ty jseš moje doggy girl, Hafo-Hafo holka
Kňučíš jako pejsek, vrčíš jak motorka (Vrr)
Když si chceme hrát, tak je to tanec, je to polka
Do postele vlezem, z postele vyleze školka (Jee)
Když děláme Hafo věci, tak mi říká Kafuu
Jsem tak sladká, chce mě lízat, jak cukrovou vatu
Když slintáme v posteli, říkáme tomu papu
Nediv se, že ukazuju zadek, že tak hafu
Baby ty jseš Hafo, baby chci tě hafo
Baby ty jseš Hafo, baby tak pojď na to
Ukazuje ass, já slintám jak pes
Hafo hafo hafo, chci jí mít nahoře bez
Baby ty jseš Hafo, baby chci tě hafo
Baby ty jseš Hafo, baby tak pojď na to
Ukazuje ass, já slintám jak pes
Hafo hafo hafo, chci jí mít nahoře bez
Ukážu ti můj zadek (h-a-a)
Ukážu ti moje candies (m-wah)
Komu se to nelíbí, ten ať si políbí
Možná si sundám i panties (ahh)
Ukážeš mi tvůj zadek (ass)
Ukážeš mi tvoje candies (m-wah)
Komu se to nelíbí, ten ať si políbí
Spolu budeme mít babies
Baby ty jseš Hafo, baby chci tě hafo
Baby ty jseš Hafo, baby tak pojď na to
Ukazuje ass, já slintám jak pes
Hafo hafo hafo, chci jí mít nahoře bez
Baby ty jseš Hafo, baby chci tě hafo
Baby ty jseš Hafo, baby tak pojď na to
Ukazuje ass, já slintám jak pes
Hafo hafo hafo, chci jí mít nahoře bez"""


