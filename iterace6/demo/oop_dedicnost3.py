"""
Jedna z nejdůležitějších věcí OOP je dědičnost. Ta nám totiž umožňuje rozšiřovat
stávající kód bez toho, aniž bychom ho museli opisovat.

Řekněme že chceme mít ještě nákladní auto a hybridní.
Jenže v podstatě jsou to jenom speciální případy obecného auta,
takže bychom zkopírovali ten stejný kód a trošku k němu přidali.

To by po čase nebylo úplně přehledné a co je nejhorší,
kdybychom chtěli udělat nějakou změnu, museli bychom to měnit na
x místech. Vždycky se snažte programy psát tak, abyste museli dělat
změnu jen na jednom místě.

A tady právě využijeme dědičnosti. Třídy od sebe mohou dědit,
což znamená, že potomek převezme všechny atributy a metody
svého rodiče, jako kdyby byly součástí jeho kódu, bez nutnosti
kopírování. Navíc je možné ponechat původní kód a přidat další.
"""

# z předchozího souboru si naimportuj třídu Auto
from oop_uvod2 import Auto


class NakladniAuto(Auto):
    """
    Od nadtřídy zdědíme tak, že její název dáme do závorek za název naší
    třídy.
    """
    def __init__(self, objem_mot, vyk, turbo, znac, mode, max_objem, spotr, naklad):
        """
        Všimni si, že do konstruktoru můžeme přidávat i další parametry - zde náklad

        Velice důležité je volání super().__init__ na PRVNÍM řádku konstruktoru -
        to nám totiž nejprve zajistí správnou inicializaci rodiče, kterou pak
        můžeme ale potřebovat dále v konstruktoru potomka - proto první řádek
        """
        super().__init__(objem_mot, vyk, turbo, znac, mode, max_objem, spotr)
        self.naklad = naklad

    def jed(self, delka):
        """
        Můžeš si všimnout, že jsem modifikoval metodu
        jed, která byla zděděná od předka. Tomu se
        říká překrývání (override) a používá se to,
        pokud nám nevyhovuje původní metoda a chceme
        ji upravit.

        Výhodou je, že je ale možné použít i původní verzi.
        K tomu opět poslouží super - tím se odkazujeme
        na nadtřídu a za ní název metody.
        """
        super().jed(delka)
        print(f"Prevazim naklad: {self.naklad}")

    def vyloz_naklad(self):
        """
        Bez problému si můžeme vytvořit novou metodu.
        """
        if self.naklad is None:
            print("Nevezu zadny naklad")
            return

        print(f"Vykladam {self.naklad}")
        self.naklad = None


class HybridniAuto(Auto):
    POHON_BENZIN = 'benzin'
    POHON_ELEKTRINA = 'elektrina'

    def __init__(self, objem_mot, vyk, turbo, znac, mode, max_objem, spotr, max_objem_baterie, el_spotr):
        super().__init__(objem_mot, vyk, turbo, znac, mode, max_objem, spotr)

        # sice se proměnné jmenují stejně, ale my je odlišíme pomocí self
        self.max_objem_baterie = max_objem_baterie
        self.baterie = self.max_objem_baterie
        self.el_spotreba = el_spotr
        self.pohon = HybridniAuto.POHON_BENZIN

    def jed(self, delka):

        print(f"{self.znacka} {self.model}:")

        zbytek = self.ujed(delka)
        if zbytek > 0:
            self.ujed(zbytek)

    def dobij(self, elektrina):
        print(f"{self.znacka} {self.model}:")
        predtim = self.baterie
        if elektrina + self.baterie > self.max_objem_baterie:
            self.baterie = self.max_objem_baterie
        else:
            self.baterie += elektrina
        po = self.baterie
        print(f"Dobito {po - predtim} kWh elektriny")

    def ujed(self, delka):
        """
        Pomocná metoda, vrací zbývající vzdálenost,
        pokud není ujeta na momentální pohon
        """
        ujeto = 0
        if self.pohon == HybridniAuto.POHON_BENZIN:
            km = self.spotreba / 100
        else:
            km = self.el_spotreba / 100

        spotrebovano = delka * km

        if self.pohon == HybridniAuto.POHON_BENZIN:
            if spotrebovano > self.nadrz:
                ujeto = self.nadrz / km
                print(f"Nadrz vyprazdnena, ujel jsem pouze {ujeto} km")
                self.nadrz = 0
                self.pohon = HybridniAuto.POHON_ELEKTRINA
            else:
                self.nadrz -= spotrebovano
                print(f"Uspesne ujeto {delka} km, stav nadrze: {self.nadrz}")

        else:
            if spotrebovano > self.baterie:
                ujeto = self.nadrz / km
                print(f"Baterie vyprazdnena, ujel jsem pouze {ujeto} km")
                self.baterie = 0
                self.pohon = HybridniAuto.POHON_BENZIN
            else:
                self.baterie -= spotrebovano
                print(f"Uspesne ujeto {delka} km, stav baterie: {self.baterie}")

        return delka - ujeto


