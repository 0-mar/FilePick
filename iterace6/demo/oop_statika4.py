"""
Vezměme si opět jenom třídu auta. Co když budeme chtít
všechny vytvořené instance očíslovat tak, aby šly čísla
postupně za sebou a byla unikátní?

Rozhodně nemůžeme použít atributy - ty jsou pro každou instanci
jiné, nehodí se tedy na společné počítadlo.

Řešením je tedy tzv. třídní proměnná (atribut). Jak název napovídá,
nepatří instanci (narozdíl od atributů), ale samotné třídě.

Co to znamená? Taková proměnná je, stejně jako samotná třída, jenom jedna.
Můžeme k ní přistupovat právě pomocí třídy.

Jako existují třídní atributy, tak existují i třídní metody. Ty má smysl
vytvářet, pokud metoda dělá to stejné bez ohledu na to, v jaké instanci bude
(typicky to bude v případě, že vůbec nepracuje s atributy). Taková metoda
se vytváří pomocí dekorátoru @staticmethod a liší se v tom, že narozdíl
od normálních metod nebere parametr self (to dává smysl, protože nemá k instanci
vůbec přístup, takže by jí self neměl kdo předat).
"""

class Auto:
    pocitadlo_id = 0

    def __init__(self):
        self.objem_motoru = 1.2
        self.vykon = 70
        self.ma_turbo = False
        self.znacka = 'Skoda'
        self.model = 'Rapid'

        self.max_objem_nadrze = 40
        self.nadrz = self.max_objem_nadrze
        self.spotreba = 5

        """
        Všimni si, jak k třídní proměnné
        přistupuju - pomocí třídy
        """
        self.id = Auto.pocitadlo_id
        Auto.pocitadlo_id += 1

    def jed(self, delka):
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

    @staticmethod
    def vyrob_aventador():
        """
        Všimni si, že metoda nebere self jako parametr
        """
        a = Auto()
        a.znacka = 'Lamborghini'
        a.model = 'Aventador'
        a.ma_turbo = True

        return a


if __name__ == '__main__':
    print(Auto.pocitadlo_id)
    a = Auto()
    print(Auto.pocitadlo_id)

    for i in range(10):
        Auto()

    print(Auto.pocitadlo_id)