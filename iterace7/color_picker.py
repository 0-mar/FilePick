import tkinter
from tkinter import Tk, ttk, font
from PIL import ImageTk, Image, ImageOps

"""
Teď si napíšeš aplikaci, která bude sloužit jako vybírátko barev. Vytvoříme
si třídu ColorPickerApp. Jako první půjdeme na konstruktor. Ten nebude brát žádné
parametry, avšak zadefinujeme v něm několik atributů:
width a height (nastavíme na 600 a 500)
root (Toplevel tkinter okno)
font (vytvoříme instanci třídy Font z modulu font, který se nachází v balíčku tkinter. 
        Nastavíme hodnotu family='Helvetica')

Rootu nastavíme titulek okna pomocí metody title(), pozadí na "black" - toho dosáhneme
pomocí metody configure, v ní nastavíme argument bg="black". Dále ještě nastavíme
velikost okna pomocí metody geometry().

Nakonec konstruktoru zavoláme metodu našeho objektu ColorPickerApp - _init_window() a metodu
rootu mainloop().


Metoda _init_window bude mít za úkol zkonstruovat celé GUI. Kromě toho v ní musíme s jednotlivými
komponentami GUI spojit reakce na různé události - například zvětšení okna vede i ke zvětšení
barevného kola.
"""


class ColorPickerApp:
    pass


if __name__ == '__main__':
    cpa = ColorPickerApp()
