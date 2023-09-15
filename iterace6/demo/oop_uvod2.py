class Auto:
    """
    Co kdybychom chtěli vytvářet instance s jinými hodnotami atributů?
    Samozřejmě bychom po vytvoření mohli všechno manuálně měnit, což je
    trošku nepraktické, ale hlavně bychom na něco mohli zapomenout.

    Proto můžeme přidat do konstruktoru parametry, které si vynutí při
    vytváření výchozí hodnoty.
    """
    def __init__(self, objem_mot, vyk, turbo, znac, mode, max_objem, spotr):
        """
        Pouze jsme použili parametry, abychom jejich hodnotu
        přiřadili atributům.
        """
        self.objem_motoru = objem_mot
        self.vykon = vyk
        self.ma_turbo = turbo
        self.znacka = znac
        self.model = mode

        self.max_objem_nadrze = max_objem
        self.nadrz = self.max_objem_nadrze
        self.spotreba = spotr

    def jed(self, delka):
        print(f"{self.znacka} {self.model}:")
        km = self.spotreba / 100
        spotrebovano = delka * km

        if spotrebovano > self.nadrz:
            print(f"Nadrz vyprazdnena, ujel jsem pouze {self.nadrz / km} km")
            self.nadrz = 0
        else:
            self.nadrz -= spotrebovano
            print(f"Uspesne ujeto {delka} km, stav nadrze: {self.nadrz}")

    def dotankuj(self, objem):
        print(f"{self.znacka} {self.model}:")
        predtim = self.nadrz
        if objem + self.nadrz > self.max_objem_nadrze:
            self.nadrz = self.max_objem_nadrze
        else:
            self.nadrz += objem
        po = self.nadrz
        print(f"Dotankovano {po - predtim} l paliva")


# můžeš si všimnout, že parametry se předávají úplně stejně, jako u metod/funkcí
porsche_gt3_rs = Auto(4, 386, True, 'Porsche', 'GT3 RS', 64, 14)
bmw_e46 = Auto(1.8, 85, False, 'BMW', 'E46', 50, 8)

porsche_gt3_rs.jed(50)
bmw_e46.jed(50)
