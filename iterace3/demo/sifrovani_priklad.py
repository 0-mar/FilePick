#!/usr/bin/python3
"""
Napiš program, který vytvoří zašifrovanou kopii souboru. Šifrování budeme provádět pomocí bitové operace XOR
tímto způsobem:

1) ze souboru označeného jako klíč přečteme 512 bajtů, které si uložíme
2) z šifrovaného souboru přečteme také blok o velikosti 512 bajtů
3) provedeme XOR mezi klíčem a přečteným blokem dat - 1. bajt klíče XORneme s 1. bajtem dat, 2. bajt
klíče s 2. bajtem dat atd.
4) zašifrovaný blok dat zapíšeme do výsledného souboru
5) postup opakujeme pro celý soubor, který šifrujeme

XOR se značí znakem ^, pokud budu chtít XORnout dvě čísla a výsledek uložit do proměnné:
xor = 5 ^ 10
Nebo pokud už mám v proměnné xor hodnotu, kterou chci na místě upravit (XORnout), můžu takto:
xor ^= 5

Doporučuju použít funkci bytearray(), která vytvoří seznam bajtů (pro postupné přidávání, bytes je immutable)

Skript se používá následujícím způsobem:
./sifrovani_priklad.py <klic> <zdroj> <cil>
kde klic je soubor s klíčem, zdroj je zdrojový soubor a cil je cílový soubor

"""
import sys


def xorcrypt(key, inp, outp):
    """
    Funkce pro šifrování souboru.

    :param key: klíč, podle kterého šifrujeme
    :param inp: cesta k originálnímu souboru
    :param outp: cesta k zašifrovanému souboru
    """
    pass


if __name__ == '__main__':
    # TODO sem přijde kód
    # nezapomen na kontrolu poctu argumentu z prikazove radky

    xorcrypt(None, None, None)
