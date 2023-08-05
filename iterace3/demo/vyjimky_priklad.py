"""
Napiš program, který dostane na vstupu (od uživatele) řetězec reprezentující šachové tahy.
Cílem je zjistit, jestli jsou všechny validní.

Řetězec bude ve tvaru: <tah>;<tah>;<tah> ..., kde tah musí být ve tvaru
[a-h][1-8] (nezáleží na velikosti písmen).

Program nakonec vypíše všechny tahy ve stejném formátu jako vstup, které
podmínku splňují.

Např. pro vstup a4;b2;ld;ag;h8 bude výstup a4;b2;h8.

Budou se hodit funkce int, split a join.

int() slouží k převedení řetězce na číslo, vyhazuje však
výjimku, pokud zadaný řetězec není číslo.
"""


