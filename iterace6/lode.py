"""
Naprogramujeme si hru lodě v Pythonu. Budeme k tomu potřebovat pár tříd -
pro reprezentaci lodí, hrací plochy na které jsou lodě umístěné, hráče a
výslednou třídu celé hry, kde vše zkompletujeme
"""

import random
import time
from typing import Set


"""
1) Třída Loď

Vytvoř třídu Lod, která bude reprezentovat jednotlivé válečné lodě.

Nejlepší bude vzít řešení, které se nabízí jako první - loď bude
jednoduše množina všech políček, které jí patří. Políčka potom
budeme reprezentovat jako dvojici čísel (souřadnic).

Třída bude mít konstruktor s jedním parametrem - umisteni,
což budou souřadnice levého horního rohu lodě (vysvětlit).
V konstruktoru vytvoříme celkem 3 atributy - zive_pole (množina všech
živých, dosud netrefených políček lodi), mrtve_pole (množina všech
mrtvých, už trefených políček lodi) a ziva (bool určující, zda je loď živá).
mrtve_pole se inicializuje na prázdnou množinu, ziva na True. zive_pole se inicializuji
statickou metodou vyber_tvar (statické metody voláme skrze třídu).

Statická metoda vyber_tvar bere jeden parametr - umisteni. Jejím úkolem je vybrat náhodný
tvar lodě a převést ho na množinu souřadnic. Tuto množinu metoda VRACÍ.
Tvary se reprezentují jako dvourozměrné pole
takto:

[
    ['X', 'X', 'X'],
    ['X', ' ', 'X'],
    ['X', 'X', 'X']
]

X představuje živé políčko lodi.
Parametr umisteni je souřadnice levého horního rohu, díky čemu si můžeme dopočítat
snadno souřadnice ostatních částí lodi (například souřadnice pravého dolního rohu
lodi bude umisteni + 2 v obou směrech osy x a y). Metoda tedy musí projít celý zadaný tvar a
postupně přidávat do výsledné množiny souřadnice živých políček.
Nejprve však musíme nějaký ten náhodný tvar vybrat. To bude jednoduché - za tím účelem
si nadefinujeme statickou konstantu TVARY, což bude pole obsahující tvary. Toto pole
zaplníme tvary, ze kterých se bude náhodně vybírat. Na začátku naší metody pak náhodně
vybereme jeden tvar pomocí random.randint() (vybereme náhodný index z pole TVARY).

Dále si ještě zadefinujeme metodu je_zive(policko), která vrátí True nebo False
v závislosti na tom, zda je políčko policko živé.

Nakonec ještě přidáme metodu na_zasah(pole), která bude ošetřovat zásah do lodi
na souřadnicích pole. Metoda nejprve vypíše zprávu:

Byla zasazena lod na miste <pole>

Odstraní pole ze živých políček a přidá je do mrtvých. Zkontroluje,
zda má loď ještě nějaká pole živá a pokud ne, nastaví atribut ziva
na False.

KONTROLNÍ SEZNAM:
- konstruktor s atributy zive_pole, mrtve_pole a ziva
metody:
- je_zive s parametrem policko
- na_zasah s parametrem pole
staticke metody:
- vyber_tvar s parametrem umisteni
staticke konstanty:
- TVARY

"""
# TODO: Lod

"""
2) Třída HraciPlocha

Teď přidáme třídu hrací plochy. Reprezentovat ji budeme (hlavně) jako
množinu lodí, které jsou na hrací ploše.

Konstruktor třídy bude mít dva parametry - pocet_lodi a velikost. Oba
parametry si budeme chtít uložit do stejně pojmenovaných atributů.
pocet_lodi určuje počet lodí na ploše, velikost potom délku strany plochy
(např. pokud bude 10, tak vzniklá plocha bude 10x10).
Dále vytvoř atribut lode, což bude množina obsahující všechny lodě na ploše
(tzn. budeme do ní ukládat objekty typu Lod). Množinu inicializuj jako prázdnou.
Nakonec konstruktoru zavolej metodu umisti_lode().

Metoda umisti_lode se bude snažit vybírat náhodná
místa na ploše pro lodě (tzn. sestaví herní plochu).
Pro každou loď (jejich počet je určen atributem pocet_lodi) vybereme
náhodné souřadnice a pak vytvoříme instanci Lodě, kterou přidáme
do množiny lode. Pro generování náhodných souřadnic zadefinujeme
pomocnou metodu vyber_pozici.

vyber_pozici bude vracet souřadnice levého horního rohu takové,
že pokud tam umístíme loď, nebude se překrývat s žádnou jinou.
Kromě náhodného výběru souřadnic tedy musíme zkontrolovat, jestli
náhodou nějaká jiná loď (její část) neleží ve čtverci, jehož levý
horní roh určují naše souřadnice. Metodu doporučuju napsat takto:

        x = ...
        y = ...

        while self.protina_lod((x, y)):
            x = ...
            y = ...

        return (x, y)
        
S tím, že místo ... přijde náhodný výběr souřadnic. Právě další
pomocná metoda protina_lod(souradnice) nám zajistí kontrolu.

Metoda protina_lod vrátí True, pokud se ve vymezeném prostoru
nachází kus jiné lodi, jinak vrátí False. Jako parametr bere
souřadnice, které právě kontrolujeme. Pro každou loď tedy musíme
vzít všechny políčka v našem čtverci 3x3 a otestovat je pomocí
metody lod.je_zive(policko). Pokud takto narazíme na živé políčko,
tak protínáme kus jiné lodi a vrátíme True. Pokud zkontrolujeme
všechny lodě a na nic nenarazíme, vracíme False.

Dále přidáme metodu vystrel_na, která bere parametr policko - souřadnice,
které se snažíme trefit. Pro každou loď pomocí metody lod.je_zive zkontrolujeme,
jestli jsme se náhodou netrefili. Pokud ano, zavoláme metodu lod.na_zasah (ta
provede věci spojené se zásahem) a pokud není loď živá (lod.ziva), snížíme
pocet_lodi o 1 a nakonec vracíme True. Jinak metoda vypíše Vedle a vrací False,
když nebyla trefena žádná loď.

Přidej ještě metodu zbyvaji_zive_lode, která vrátí True, pokud ještě jsou
nějaké lodi naživu, jinak vrací False.

Úplně nakonec si přidáme metodu vykresli, která nám bude vykreslovat herní
plochu. Za tímto účelem si přidáme 3 třídní atributy - ZIVE_POLE, MRTVE_POLE A PRAZDNE_POLE.
Jejich hodnoty si nastavte tak, jak chcete aby se zobrazovala tato políčka. Já mám O, X a mezeru.
Vykreslování nejlépe vyřešíme tak, že si předpřipravíme prázdnou mřížku (dvojrozměrné pole naplněné
hodnotami PRAZDNE_POLE). Poté pro každou loď projdi všechna živá a mrtvá pole a na jejich souřadnice
vlož v našem poli hodnotu ZIVE_POLE a MRTVE_POLE.
Následně vypiš Lodi nazivu: <pocet_lodi>.
Na konec  zavolej pomocnou metodu vykresli_plochu(plocha). Ta jako parametr bere naše dvojrozměrné
pole. Plocha by měla být vykreslena nějak takhle:

     a   b   c   d   e   f   g   h   i   j 
   +---+---+---+---+---+---+---+---+---+---+
1  |   |   |   |   |   | O | O | O |   |   |  1
   +---+---+---+---+---+---+---+---+---+---+
2  |   |   |   |   |   | O |   | O |   |   |  2
   +---+---+---+---+---+---+---+---+---+---+
3  |   |   |   |   |   | O | O | O |   |   |  3
   +---+---+---+---+---+---+---+---+---+---+
4  |   |   |   |   |   |   |   |   |   |   |  4
   +---+---+---+---+---+---+---+---+---+---+
5  |   |   |   |   |   |   |   |   |   |   |  5
   +---+---+---+---+---+---+---+---+---+---+
6  |   | O | O | O |   |   |   |   |   |   |  6
   +---+---+---+---+---+---+---+---+---+---+
7  |   | O |   | O |   | O |   |   |   |   |  7
   +---+---+---+---+---+---+---+---+---+---+
8  |   | O | O | O |   | O |   |   |   |   |  8
   +---+---+---+---+---+---+---+---+---+---+
9  |   |   |   |   | O | O | O |   |   |   |  9
   +---+---+---+---+---+---+---+---+---+---+
10 |   |   |   |   |   |   |   |   |   |   |  10
   +---+---+---+---+---+---+---+---+---+---+
     a   b   c   d   e   f   g   h   i   j 
     
KONTROLNÍ SEZNAM:
- konstruktor s parametry pocet_lodi, velikost
              s atributy pocet_lodi, velikost, lode
metody:
- umisti_lode
- vyber_pozici s parametrem pole
- protina_lod s parametrem souradnice
- vystrel_na s parametrem souradnice
- zbyvaji_zive_lode
- vykresli
- vykresli_plochu s parametrem plocha

staticke atributy:
- ZIVE_POLE
- MRTVE_POLE
- PRAZDNE_POLE
"""

# TODO: HraciPlocha

"""
3) Třída Hrajici

Tato třída bude sloužit jako společný základ pro robotického
a lidského hráče.

Konstruktor třídy obsahuje 3 parametry - nick, pocet_lodi, velikost_plochy.
Nick si uložíme do stejnojmenného atributu, pocet_lodi a velikost_plochy
použijeme jako argumenty při vytváření instance HraciPlochy - tu uložíme
do dalšího atributu plocha.

Dále zadefinujeme metodu hraj s parametrem nepratelska_plocha. Ta bude
mít následující tělo:

        print("═" * 60)
        print(f"Tah {self.nick}:")
        print("═" * 60)

        souradnice = self.nacti_souradnice()
        self.vystrel(souradnice, nepratelska_plocha)
        
Tato metoda poslouží jako hlavní bod pro ovládání robotického i lidského hráče.

Bude tedy potřeba přidat metodu nacti_souradnice. Ta bude ve výchozí implementaci
vracet (-1, -1).

Dále přidáme metodu vystrel s parametry souradnice a nepratelska_plocha.
Tato metoda pouze vypíše hlášku:

Strilim na pozici <souradnice>...

Nakonec ještě přidáme metodu je_nazivu. Ta vrátí výsledek metody
zbyvaji_zive_lode z instance hrací plochy (self.plocha).

KONTROLNÍ SEZNAM:
- konstruktor s parametry nick, pocet_lodi, velikost_plochy
              s atributy nick, plocha
metody:
- hraj s parametrem nepratelska_plocha
- nacti_souradnice
- vystrel s parametry souradnice a nepratelska_plocha
- je_nazivu
"""

# TODO: Hrajici

"""
4) Třída Hrac

Tato třída reprezentuje lidského hráče. Hrac rozšiřuje (dědí z) třídy Hrajici.

Jako její rodič má třída konstruktor s parametry nick, pocet_lodi, velikost_plochy.
Podstatným rozdílem však je, že jako PRVNÍ řádek konstruktoru bude volání konstruktoru
nadtřídy. To je proto, že je nejprve potřeba nainicializovat rodičovský objekt a až
potom se pustíme do konstrukce našeho objektu. Po volání rodičovského konstruktoru
vytvoříme dva další atributy (prázdné množiny) trefena_prazdna_pole a trefena_ziva_pole.
Do nich si budeme ukládat trefená pole podle kategorií.

Dále překryjeme metodu hraj z nadtřídy. Jako první řádek bude volání verze metody z
nadtřídy (super().hraj(nepratelska_plocha)). Chceme totiž využít i původní metodu
hraj. Dále metoda vypíše hlášku:

Moje rozmisteni:

a poté zavolá metodu vykresli atributu plocha. To je možné udělat, protože atribut
plocha jsme zdědili z nadtřídy a tudíž ho máme k dispozici. Nakonec ještě zavolej
funkci sleep s argumentem 3 z modulu time (který je potřeba naimportovat).

Překryjeme i metodu vystrel. Opět zavoláme nejprve verzi metody z nadtřídy.
Na parametru nepratelska_plocha zavoláme metodu vystrel_na s argumentem souradnice.
Důležité je si uložit výsledek tohoto volání do nějaké proměnné, pojmenujeme ji třeba
trefeno. Pokud je trefeno True -> trefili jsme nepřátelskou loď, přidáme souradnice
do množiny trefených živých (trefena_ziva_pole). Pokud je trefeno False, přidáme
souradnice do množiny trefených prázdných (trefena_prazdna_pole).

Dále překryjeme metodu nacti_souradnice. Na začátku metody vypíšeme hlášku

Moje strely:

a zavoláme metodu vykresli_trefeno (k ní se dostaneme vzápětí).
Následovat bude načítání souřadnic ze standardního vstupu s touto hláškou:

Zadej souradnice strely ve tvaru <pismeno><cislo>:

Toto dotazování neskončí do té doby, než nebudou zadány validní souřadnice.
Jejich validitu bude kontrolovat metoda validni_souradnice s parametrem souradnice (a vrátí
True nebo False v závislosti na tom, jestli jsou validní nebo ne).
Ve výsledku tedy metoda nacti_souradnice vrací validní souřadnice, které je nakonec uživatel
donucen zadat.
Označení souřadnic je v rozsahu [a, a + velikost plochy - 1] a [1, velikost plochy - 1].
Také je potřeba ošetřit případ, kde není číslo v místě, kde je očekávané.

Nakonec přidáme metodu vykresli_trefeno. Ta stejným způsobem, jako je popsáno ve
třídě HraciPlocha, vytvoří dvojrozměrný seznam, akorát ho bude plnit dvěma jinými konstantami -
TREFENO_ZIVE a TREFENO_PRAZDNE (budeme procházet množiny trefena_prazdna_pole a trefena_ziva_pole).
TREFENO_ZIVE bude reprezentovat trefené políčka lodí, zatímco TREFENO_PRAZDNE bude reprezentovat
políčka prázdná. Já je mám nastavené na X a *. Tento seznam vykreslíme zavoláním metody
vykresli_plochu na atributu plocha (zde je vidět výhoda dekompozice na menší funkce).

     a   b   c   d   e   f   g   h   i   j 
   +---+---+---+---+---+---+---+---+---+---+
1  |   |   |   |   |   |   |   |   |   |   |  1
   +---+---+---+---+---+---+---+---+---+---+
2  |   |   |   |   |   |   |   |   |   |   |  2
   +---+---+---+---+---+---+---+---+---+---+
3  |   |   |   |   |   |   |   |   |   |   |  3
   +---+---+---+---+---+---+---+---+---+---+
4  |   |   |   |   |   |   |   |   |   |   |  4
   +---+---+---+---+---+---+---+---+---+---+
5  |   |   |   |   | * |   |   | * |   |   |  5
   +---+---+---+---+---+---+---+---+---+---+
6  |   |   |   |   | * |   |   | X | X |   |  6
   +---+---+---+---+---+---+---+---+---+---+
7  |   |   |   |   |   |   |   |   |   |   |  7
   +---+---+---+---+---+---+---+---+---+---+
8  |   |   |   |   |   |   |   |   |   |   |  8
   +---+---+---+---+---+---+---+---+---+---+
9  |   |   |   |   |   |   |   |   |   |   |  9
   +---+---+---+---+---+---+---+---+---+---+
10 |   |   |   |   |   |   |   |   |   |   |  10
   +---+---+---+---+---+---+---+---+---+---+
     a   b   c   d   e   f   g   h   i   j 

KONTROLNÍ SEZNAM:
- konstruktor s parametry nick, pocet_lodi, velikost_plochy
              s atributy trefena_prazdna_pole, trefena_ziva_pole
metody:
- překrýt hraj
- překrýt vystrel
- překrýt nacti_souradnice
- vykresli_trefeno
- validni_souradnice s parametrem souradnice

staticke atributy:
- TREFENO_ZIVE
- TREFENO_PRAZDNE
"""

# TODO: Hrac


"""
5) Třída Robot

Tato třída reprezentuje robota. Robot rozšiřuje (dědí z) třídy Hrajici.

Jako její rodič má třída konstruktor s parametry nick, pocet_lodi, velikost_plochy.
Opět jako PRVNÍ řádek konstruktoru bude volání konstruktoru nadtřídy. Kromě toho
ještě vytvoř atribut netrefena_pole. V této množině se budou nacházet všechna netrefená
políčka nepřátelské hrací plochy. Přiřaď mu prázdnou množinu jako hodnotu. Poté však
naplň množinu všemi políčky z hrací plochy. Toho docílíme pomocí 2 vložených for cyklů
do sebe - ty nám umožní vygenerovat všechny kombinace souřadnic.

Poté překryj metodu hraj. Opět na prvním řádku zavolej implementaci z nadtřídy. Pro
ladící účely přidej ještě vykreslení robotovy hrací plochy na konec metody.

Musíme také překrýt metodu nacti_souradnice. Ta bude u robota fungovat tak, že vybere
náhodné políčko, na které dosud nebylo vystřeleno. Na výběr náhodného prvku ze seznamu
můžeme použít funkci random.choice, avšak my máme množinu. Proto musíme nejprve převést
množinu na seznam pomocí funkce list. Náhodné souřadnice poté metoda nacti_souradnice vrátí.

Dále překryjeme metodu vystrel. Opět na prvním řádku metody voláme implementaci z rodiče.
Aby bylo lépe vidět co se děje, přidáme malou pauzu - zavoláme funkci sleep z modulu
time s argumentem 2. Potom odstraníme z množiny netrefených políček souradnice.
Nakonec zavoláme na atributu nepratelska_plocha metodu vystrel_na s argumentem souradnice.

KONTROLNÍ SEZNAM:
- konstruktor s parametry nick, pocet_lodi, velikost_plochy
              s atributy netrefena_pole
metody:
- překrýt hraj
- překrýt nacti_souradnice
- překrýt vystrel
"""

# TODO: Robot


"""
6) Třída Lode

Tato třída reprezentuje výslednou hru.

Konstruktor má 2 parametry - hrac1 a hrac2. Tyto parametry si
uložíme do stejnojmenných atributů. Zároveň oba dva hráče
ještě uložíme do seznamu, který pojmenujeme hraci. Ten se
bude hodit pro jednodušší střídání tahů.

Pak vytvoříme metodu spust_hru. Ta bude mít následující tělo:

        index = 0
        while self.pokracuje_hra():
            nepratelska_plocha = self.hraci[(index + 1) % len(self.hraci)].plocha
            self.hraci[index % len(self.hraci)].hraj(nepratelska_plocha)
            index += 1

        vitez = self.vitez_hry()

        print()
        print()
        print(f"Vitez je: {vitez.nick}")
        print(f"Zbylych zivych lodi: {vitez.plocha.pocet_lodi}")
        print(f"Konecne rozlozeni: ")
        vitez.plocha.vykresli()
        
Aby fungovala, musíme doimplementovat pomocné metody.

První je pokracuje_hra, která zkontroluje, jestli má vůbec smysl začínat tah.
Tato metoda vrátí True, pokud jsou alespoň 2 hráči naživu. K tomu se bude
hodit metoda hrac.je_nazivu.

Druhá pomocná metoda je vitez_hry. Ta vrátí posledního živého hráče ze seznamu hraci.

KONTROLNÍ SEZNAM:
- konstruktor s parametry hrac1, hrac2
              s atributy hrac1, hrac2, hraci
metody:
- spust_hru
- pokracuje_hra
- vitez_hry
"""
# TODO: Lode


if __name__ == '__main__':
    #lode = Lode(Hrac("pepa", 3, 10), Robot("robondra", 3, 10))
    #lode.spust_hru()
    pass
