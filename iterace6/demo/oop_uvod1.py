"""
OOP (objektově orientované programování) je způsob, jakým psát programy tak,
abychom se v nich přiblížili k modelu reálného světa. To je výhodné
hned z několika důvodů:

- lépe se nad problémem přemýšlí
- program se sestává z oddělených komponent - celků (objektů), které spolu kominukují
- jednodušší přidávání nových featur (pokud je program dobře navržen)

Objekty se "modelují" pomocí 2 nástrojů - atributů a metod.

Atributy jsou data, které objekty uchovávají - kdybychom modelovali
nějaký systém s uživateli, tak bychom si chtěli u každého uživatele
pamatovat jeho jméno, heslo, osobní údaje atp.

Metody zase říkají, co daný objekt umí a jak se chová.
Například u uživatele bychom chtěli mít schopnost přihlašovat se,
odhlašovat se, měnit heslo.

Metody nejsou nic jiného než funkce uvnitř tříd.

Všem funkcím definovaným uvnitř třídy se říká metody.
Ty se oproti funkcím liší jednou věcí - berou jako
první parametr odkaz na objekt, ze kterého byly zavolány.

Podle konvence se tento parametr pojmenovává self.
"""


class Auto:
    """
    Základem OOP jsou tzv. třídy. To jsou vzory (plánky), podle kterých se vytváří
    objekty. Takto vytvořeným objektům se říká instance.

    Zde máme vytvořenou třídu Auto.
    """
    def __init__(self):
        """
        Metoda __init__ je jedna z nejdůležitějších metod, protože
        je volána během vytváření instance objektu. V ní se poté
        dělají všechny věci spojené s úvodním nastavováním objektu,
        jako je vytvoření atributů.

        Každá instance má vlastní hodnoty atributů - nejsou nijak sdílené
        mezi instancemi, každá si tedy uchovává vlastní stav.

        Atribut vytvoříme pomocí parametru self a názvu atributu,
        odděleným tečkou. Stejným způsobem můžeme přistupovat k
        uložené hodnotě.

        Jak přesně funguje proces vytváření nových objektů se dočtete tady:
        https://realpython.com/python-class-constructor/
        """
        self.objem_motoru = 1.2
        self.vykon = 70
        self.ma_turbo = False
        self.znacka = 'Skoda'
        self.model = 'Rapid'

        self.max_objem_nadrze = 40
        self.nadrz = self.max_objem_nadrze
        self.spotreba = 5

    def jed(self, delka):
        """
        Všimněte si, že metoda má opět jako 1. parametr self a poté
        následují normální parametry.
        """
        km = self.spotreba / 100
        spotrebovano = delka * km

        if spotrebovano > self.nadrz:
            print(f"Nadrz vyprazdnena, ujel jsem pouze {self.nadrz / km} km")
            self.nadrz = 0
        else:
            self.nadrz -= spotrebovano
            print(f"Uspesne ujeto {delka} km, stav nadrze: {self.nadrz}")

    def dotankuj(self, objem):
        predtim = self.nadrz
        if objem + self.nadrz > self.max_objem_nadrze:
            self.nadrz = self.max_objem_nadrze
        else:
            self.nadrz += objem
        po = self.nadrz
        print(f"Dotankovano {po - predtim} l paliva")

"""
Tímto způsobem si vytvoříme objekt (instanci) podle návodu (třídy).
Instance je normální proměnná jako kterákoliv jiná.
"""
rapid = Auto()
# Pomocí tečkové notace voláme metody na objektu
rapid.jed(750)
rapid.jed(150)
rapid.dotankuj(80)

# pomocí tečkové notace máme i přístup k atributům
rapid.max_objem_nadrze = 80
rapid.dotankuj(40)
