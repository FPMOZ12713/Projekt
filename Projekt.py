from tkinter import *
import datetime
from sqlite3 import *
import tkinter.messagebox

x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


root = Tk()
root.title("Rezervacija kino ulaznica")



mainFrame = Frame(root)
mainFrame.pack(padx = 15, pady = 15)

conn = connect('filmovi_popis.db')
c = conn.cursor()


Var = StringVar(root)
izbor = {"Akcija", "Komedija", "Drama", "Horor"}
Var.set("Akcija")
varr="Akcija"
def promjena(*args):
    varr= Var.get()
    print (varr)
Var.trace("w", promjena)


popUp = OptionMenu( mainFrame, Var, *izbor)
theLabel = Label(mainFrame, text="Odaberite žanr filma"). grid(row = 1, column = 1)
popUp.grid(row=2, column=1, pady = 15)




Label1 = Label(mainFrame, text = "Unesite/kopirajte naslov željenog filma: "). grid(row = 4, column = 1, pady = 5)
polje1 = Entry(mainFrame)
polje1.grid(row = 5, column = 1, padx=60, pady = 10, ipadx = 40)

Label2 = Label(mainFrame, text = "Unesite svoje ime: "). grid(row = 6, column = 1, sticky = "W", pady = 10)
polje2 = Entry(mainFrame)
polje2.grid(row = 7, column = 1, sticky = "W", ipadx = 35)
Label4 = Label(mainFrame, text = "Broj karata: "). grid(row = 6, column = 1, sticky = "E", padx = 40)
polje3 = Entry(mainFrame)
polje3.grid(row = 7, column = 1, sticky = "E")


T = Listbox(mainFrame, height = 9, width = 53,font=("Times New Roman", 12), selectmode="single")
T.grid(row = 3, column = 1, sticky = "N")
T.insert(0 , )



izlaz = Button(root, text = "IZLAZ", command=quit)
izlaz.pack(side = "left")

LabelD = Label(mainFrame, text = x)
LabelD.grid(row = 9, column = 1)


def izbor():
    a = c.execute('SELECT *FROM filmovi WHERE zanr = "?"', (Var.get()))
    #c.execute("SELECT * FROM filmovi WHERE zanr = 'Akcija'")
    podaci = c.fetchall()

    for a in podaci:
        T.insert(1, a)

    conn.commit()

Button1 = Button(mainFrame, text="Osvježi", command=izbor)
Button1.grid(row = 2, column = 1, sticky = "E")

def rezervacija():
    film = polje1.get()
    ime = polje2.get()
    broj = polje3.get()
    S = ime+" "+"rezervirali ste sljedeći broj karata: "+" "+broj+"  "+"za film:"+film
    REZ = ime+" "+film+" "+broj
    tkinter.messagebox.showinfo('INFO', S)
    f = open("rezervacije", "a")
    f.write("\n"+REZ)
    f.close()

dugme = Button(root, text="REZERVIRAJ", command = rezervacija)
dugme.pack(side = "right")

root.mainloop()
