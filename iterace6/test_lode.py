"""
Spusť tento skript pro kontrolu řešení.
"""

from lode import *


def test_lod_class():
    print("=" * 33)
    print("Test třídy Lod")
    print("=" * 33)
    lod = Lod((1, 0))

    try:
        lod.zive_pole
        assert lod.zive_pole != set(), "Živá pole by neměla být prázdná po vytvoření"
    except AttributeError:
        print("Třída nemá atribut ziva_pole")
        exit(1)

    try:
        lod.mrtve_pole
        assert lod.mrtve_pole == set(), "Mrtvá pole by měla být prázdná po vytvoření"
    except AttributeError:
        print("Třída nemá atribut mrtve_pole")
        exit(1)

    try:
        lod.ziva
        assert lod.ziva, "Loď by měla být po vytvoření živá"
    except AttributeError:
        print("Třída nemá atribut ziva")
        exit(1)

    try:
        Lod.TVARY

        Lod.TVARY = [[['X', 'X', 'X'],
              ['X', ' ', 'X'],
              ['X', 'X', 'X']
              ]]

        assert Lod.vyber_tvar((3, 0)) == {(3, 0), (4, 0), (5, 0), (3, 1), (5, 1), (3, 2), (4, 2), (5, 2)}

    except AttributeError:
        print("Třída nemá statickou konstantu TVARY")
        exit(1)

    try:
        Lod.vyber_tvar
    except AttributeError:
        print("Třída nemá statickou metodu vyber_tvar")
        exit(1)

    try:
        lod.na_zasah

        l = Lod((0, 0))
        l.zive_pole.clear()
        l.zive_pole.add((0, 0))
        l.na_zasah((0, 0))

        assert l.zive_pole == set(), "Po zásahu by měla být živá pole prázdná"
        assert l.mrtve_pole == {(0, 0)}, "Po zásahu by měla mrtvá pole obsahovat {0, 0}"
        assert not l.ziva, "Po zásahu by měla být loď mrtvá"

    except AttributeError:
        print("Třída nemá metodu na_zasah")
        exit(1)

    try:
        lod.je_zive

        l = Lod((0, 0))
        l.zive_pole.clear()
        l.zive_pole.add((0, 0))

        assert l.je_zive((0, 0))
        assert not l.je_zive((1, 0))

    except AttributeError:
        print("Třída nemá metodu je_zive")
        exit(1)

    print("=" * 35)
    print("Test třídy Lod proběhl v pořádku.")
    print("=" * 35)


def test_hraci_plocha_class():
    print("=" * 35)
    print("Test třídy HraciPlocha")
    print("=" * 35)

    Lod.TVARY = [[['X', 'X', 'X'],
                  ['X', ' ', 'X'],
                  ['X', 'X', 'X']
                  ]]
    hp = HraciPlocha(1, 3)

    try:
        hp.pocet_lodi
        assert hp.pocet_lodi == 1, "Špatně nastavený počet lodí"
    except AttributeError:
        print("Třída nemá atribut pocet_lodi")
        exit(1)

    try:
        hp.velikost
        assert hp.velikost == 3, "Špatně nastavená velikost"
    except AttributeError:
        print("Třída nemá atribut velikost")
        exit(1)

    try:
        hp.lode

        assert len(hp.lode) == 1, "Množina by měla obsahovat jednu loď"
        for lod in hp.lode:
            assert lod.zive_pole == {(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)}, "Loď byla špatně vytvořená"

    except AttributeError:
        print("Třída nemá atribut lode")
        exit(1)

    try:
        hp.umisti_lode
    except AttributeError:
        print("Třída nemá metodu umisti_lode")
        exit(1)

    try:
        hp.vyber_pozici
    except AttributeError:
        print("Třída nemá metodu vyber_pozici")
        exit(1)

    try:
        hp.protina_lod

        assert hp.protina_lod((0, 0))
        assert hp.protina_lod((1, 1))
    except AttributeError:
        print("Třída nemá metodu protina_lod")
        exit(1)

    try:
        hp.vystrel_na

        for i in range(3):
            for j in range(3):
                if (i, j) != (1, 1):
                    assert hp.vystrel_na((i, j)), "Trefení živého pole by mělo vrátit True"
                else:
                    assert not hp.vystrel_na((i, j)), "Střela vedle by měla vrátit False"

        for lod in hp.lode:
            assert lod.mrtve_pole == {(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)}

        assert hp.pocet_lodi == 0, "Loď by měla být mrtvá"

    except AttributeError:
        print("Třída nemá metodu vystrel_na")
        exit(1)

    try:
        hp.zbyvaji_zive_lode

        assert not hp.zbyvaji_zive_lode()
    except AttributeError:
        print("Třída nemá metodu zbyvaji_zive_lode")
        exit(1)

    try:
        hp.vykresli
    except AttributeError:
        print("Třída nemá metodu vykresli")
        exit(1)

    try:
        hp.vykresli_plochu
    except AttributeError:
        print("Třída nemá metodu vykresli_plochu")
        exit(1)

    print("=" * 35)
    print("Test třídy HraciPlocha proběhl v pořádku.")
    print("=" * 35)


def test_hrajici_class():
    print("=" * 35)
    print("Test třídy Hrajici")
    print("=" * 35)

    Lod.TVARY = [[['X', 'X', 'X'],
                  ['X', ' ', 'X'],
                  ['X', 'X', 'X']
                  ]]
    hrajici = Hrajici("pepa", 1, 3)
    try:
        hrajici.nick
    except AttributeError:
        print("Třída nemá atribut nick")
        exit(1)

    try:
        hrajici.plocha
    except AttributeError:
        print("Třída nemá atribut plocha")
        exit(1)

    try:
        hrajici.hraj
    except AttributeError:
        print("Třída nemá metodu hraj")
        exit(1)

    try:
        hrajici.je_nazivu
        assert hrajici.je_nazivu(), "Hrac by mel byt nazivu"
    except AttributeError:
        print("Třída nemá metodu je_nazivu")
        exit(1)

    try:
        hrajici.nacti_souradnice
    except AttributeError:
        print("Třída nemá metodu nacti_souradnice")
        exit(1)

    try:
        hrajici.vystrel
    except AttributeError:
        print("Třída nemá metodu vystrel")
        exit(1)

    print("=" * 35)
    print("Test třídy Hrajici proběhl v pořádku.")
    print("=" * 35)


def test_hrac_class():
    print("=" * 35)
    print("Test třídy Hrac")
    print("=" * 35)

    Lod.TVARY = [[['X', 'X', 'X'],
                  ['X', ' ', 'X'],
                  ['X', 'X', 'X']
                  ]]
    hrac = Hrac("pepa", 1, 3)
    if not isinstance(hrac, Hrajici):
        print("Třída není podtřídou Hrajici")
        exit(1)

    try:
        hrac.trefena_prazdna_pole
        hrac.vystrel((1, 1), hrac.plocha)
        assert hrac.trefena_prazdna_pole == {(1, 1)}
    except AttributeError:
        print("Třída nemá atribut trefena_prazdna_pole")
        exit(1)

    try:
        hrac.trefena_ziva_pole
        hrac.vystrel((0, 0), hrac.plocha)
        assert hrac.trefena_ziva_pole == {(0, 0)}
    except AttributeError:
        print("Třída nemá atribut trefena_ziva_pole")
        exit(1)

    try:
        hrac.nacti_souradnice
    except AttributeError:
        print("Třída nemá metodu nacti_souradnice")
        exit(1)

    try:
        hrac.validni_souradnice
        for i, n in enumerate(range(1, 4)):
            pismenko = chr(ord('a') + i)
            assert hrac.validni_souradnice(pismenko + str(n))
        assert not hrac.validni_souradnice("d1")
        assert not hrac.validni_souradnice("a0")
        assert not hrac.validni_souradnice("b4")
        assert not hrac.validni_souradnice("xd")
        assert not hrac.validni_souradnice("1a")

    except AttributeError:
        print("Třída nemá metodu validni_souradnice")
        exit(1)

    try:
        hrac.vykresli_trefeno
    except AttributeError:
        print("Třída nemá metodu vykresli_trefeno")
        exit(1)

    print("=" * 35)
    print("Test třídy Hrac proběhl v pořádku.")
    print("=" * 35)


def test_robot_class():
    print("=" * 35)
    print("Test třídy Robot")
    print("=" * 35)

    Lod.TVARY = [[['X', 'X', 'X'],
                  ['X', ' ', 'X'],
                  ['X', 'X', 'X']
                  ]]
    robot = Robot("pepa", 1, 3)
    if not isinstance(robot, Hrajici):
        print("Třída není podtřídou Hrajici")
        exit(1)

    print("=" * 35)
    print("Test třídy Robot proběhl v pořádku.")
    print("=" * 35)


def test_lode_class():
    print("=" * 35)
    print("Test třídy Lode")
    print("=" * 35)

    l = Lode(Hrac("pepa", 1, 3), Robot("robondra", 1, 3))
    try:
        l.hrac1
    except AttributeError:
        print("Třída nemá atribut hrac1")
        exit(1)

    try:
        l.hrac2
    except AttributeError:
        print("Třída nemá atribut hrac2")
        exit(1)

    try:
        l.hraci
    except AttributeError:
        print("Třída nemá atribut hraci")
        exit(1)

    try:
        l.spust_hru
    except AttributeError:
        print("Třída nemá metodu spust_hru")
        exit(1)

    try:
        l.pokracuje_hra

        assert l.pokracuje_hra()
    except AttributeError:
        print("Třída nemá metodu pokracuje_hra")
        exit(1)

    try:
        l.vitez_hry
    except AttributeError:
        print("Třída nemá metodu vitez_hry")
        exit(1)

    print("=" * 35)
    print("Test třídy Lode proběhl v pořádku.")
    print("=" * 35)


if __name__ == '__main__':
    test_lod_class()
    test_hraci_plocha_class()
    test_hrajici_class()
    test_hrac_class()
    test_robot_class()
    test_lode_class()
