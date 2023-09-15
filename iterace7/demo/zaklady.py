import tkinter
from tkinter import Tk, ttk

# vytvoř top-level okno
root = Tk()

# změň pozadí na červenou
root['bg'] = 'red'  # nebo root.configure(background="red")

# zajistí, že se obsah okna bude roztahovat ve všech směrech se sanotným oknem
# (na šířku i na výšku zabere obsah toplevel okna dodatečné místo)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Do hlavního okna umisťujeme jako kontejner rámeček.
# Díky columnconfigure a rowconfigure se může roztahovat s oknem.
frm = ttk.Frame(root, padding=10)

# Důležitá je však možnost sticky. Ta říká, na jakých stranách buňky
# se má widget přichytávat (nwes = north, west, east, south).

# Pomocí column a row widget umístíme. Můžeme si okno představit jako
# pomyslnou mřížku s buňkami - do buněk umisťujeme widgety.
# Pomocí columnconfigure pak ovlivňujeme, jak se buňky roztahují.
frm.grid(column=0, row=0, sticky='nwes')

frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)

popisek = tkinter.Label(frm, text="Hello World!")
popisek.grid(column=0, row=0, sticky='nswe')

frm.rowconfigure(1, weight=1)

tlacitko = tkinter.Button(frm, text="Quit", command=root.destroy)
tlacitko.grid(column=0, row=1, sticky='nswe')

root.mainloop()