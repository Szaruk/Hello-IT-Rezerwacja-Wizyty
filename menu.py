from database import *
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Dodaj klienta")
root.iconbitmap("img/server.ico")
root.geometry("400x600")
Label(root, text="Dodaj klienta", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)

def clear():
    imie_klienta_box.delete(0, END)
    nazwisko_klienta_box.delete(0, END)
    nr_tel_klienta_box.delete(0, END)
    pesel_klienta_box.delete(0, END)


def dodaj_klienta(imie_klienta, nazwisko_klienta, nr_tel_klienta, pesel_klienta):
    imie_klienta = imie_klienta_box.get()
    nazwisko_klienta = nazwisko_klienta_box.get()
    nr_tel_klienta = nr_tel_klienta_box.get()
    pesel_klienta = pesel_klienta_box.get()
    id_klienta = cur.execute("SELECT id_klienta FROM klienci WHERE imie = ? AND nazwisko = ?", (imie_klienta, nazwisko_klienta))
    id_klienta = cur.fetchone()
    if id_klienta == None:
        cur.execute("INSERT INTO klienci VALUES(NULL,?,?,?,?);",(imie_klienta, nazwisko_klienta, nr_tel_klienta, pesel_klienta))
        Label(root, text="Dodano klienta").grid(row=0, column=2)
    else:
        Label(root, text="Taki klient istnieje").grid(row=0, column=2)
    clear()
    con.commit()

def edytuj_klienta():
    root_edutuj = Tk()
    root_edutuj.title("Edytuj klienta")
    root_edutuj.iconbitmap("img/server.ico")
    root_edutuj.geometry("800x600")


def wyswiel_klienci():
    root_klienci = Tk()
    root_klienci.title("Dodaj klienta")
    root_klienci.iconbitmap("img/server.ico")
    root_klienci.geometry("800x600")
    #Label(root_klienci, text="Lista klientów", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)
    id_klienta = cur.execute("SELECT id_klienta FROM klienci")
    id_klienta = cur.fetchone()
    if id_klienta == None:
        Label(root_klienci, text="Nie ma klientów").grid(row=1, column=0)
    else:
        cur.execute("SELECT * FROM klienci")
        baza = cur.fetchall()
        Label(root_klienci, text="ID", borderwidth=2, relief="groove", width=15).grid(row=0, column=0)
        Label(root_klienci, text="IMIE", borderwidth=2, relief="groove", width=15).grid(row=0, column=1)
        Label(root_klienci, text="NAZWISKO", borderwidth=2, relief="groove", width=15).grid(row=0, column=2)
        Label(root_klienci, text="NUMER TELEFONU", borderwidth=2, relief="groove", width=15).grid(row=0, column=3)
        Label(root_klienci, text="PESEL", borderwidth=2, relief="groove", width=15).grid(row=0, column=4)
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_klienci, text=y, borderwidth=2, relief="groove", width=15)
                dane_label.grid(row=index+2, column=num)
                num+=1

def wyszukaj_klienta():
    global root_wyszukaj
    root_wyszukaj = Tk()
    root_wyszukaj.title("Lista klientów")
    root_wyszukaj.iconbitmap("img/server.ico")
    root_wyszukaj.geometry("800x600")
    lista_wyboru = ttk.Combobox(root_wyszukaj, value=['Wybierz...', 'Imie', 'Nazwisko', 'Numer telefonu', 'Pesel'])
    lista_wyboru.current(0)
    lista_wyboru.grid(row=0, column=3)
    #wybor = lista_wyboru.get()
    wyszukaj_label = Label(root_wyszukaj, text="Wyszukaj klienta").grid(row=0, column=1, padx=5, pady=5, sticky=W)
    wyszukaj_box = Entry(root_wyszukaj)
    wyszukaj_box.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    wyszukaj_button = Button(root_wyszukaj, text='Wyszukaj', command=lambda: wyszukaj(wyszukaj_box, lista_wyboru)).grid(row=1, column=0, columnspan=2)

def wyszukaj(wyszukaj_box, lista_wyboru):
    wybor_listy = lista_wyboru.get()
    wyszukane_dane = wyszukaj_box.get()
    if wybor_listy == 'Wybierz...':
        Label(root_wyszukaj, text="Brak wyboru z listy").grid(row=3, column=0, columnspan=2)
    elif wybor_listy == 'Imie':
        cur.execute("SELECT * FROM klienci WHERE imie = ?", (wyszukane_dane,))
        baza = cur.fetchall()
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_wyszukaj, text=y)
                dane_label.grid(row=index + 3, column=num, columnspan=2)
                num += 1
    elif wybor_listy == 'Nazwisko':
        cur.execute("SELECT * FROM klienci WHERE nazwisko = ?", (wyszukane_dane,))
        baza = cur.fetchall()
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_wyszukaj, text=y)
                dane_label.grid(row=index + 3, column=num, columnspan=2)
                num += 1
    elif wybor_listy == 'Numer telefonu':
        cur.execute("SELECT * FROM klienci WHERE numer_tel = ?", (wyszukane_dane,))
        baza = cur.fetchall()
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_wyszukaj, text=y)
                dane_label.grid(row=index + 3, column=num, columnspan=2)
                num += 1
    elif wybor_listy == 'Pesel':
        cur.execute("SELECT * FROM klienci WHERE pesel = ?", (wyszukane_dane,))
        baza = cur.fetchall()
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_wyszukaj, text=y)
                dane_label.grid(row=index + 3, column=num, columnspan=2)
                num += 1

def dodaj_zwierzaka():
    global root_dodaj_zwierzaka
    root_dodaj_zwierzaka = Tk()
    root_dodaj_zwierzaka.title("Dodaj zwierzaka")
    root_dodaj_zwierzaka.iconbitmap("img/server.ico")
    root_dodaj_zwierzaka.geometry("800x600")
    Label(root_dodaj_zwierzaka, text="Dodaj zwierzaka", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)

    global imie_zwierzak_box
    imie_zwierzak = Label(root_dodaj_zwierzaka, text=("Imie"), font=("Helvetica", 11)).grid(row=1, column=0, sticky=W, padx=5)
    imie_zwierzak_box = Entry(root_dodaj_zwierzaka)
    imie_zwierzak_box.grid(row=1, column=1)

    global gatunek_zwierzaka_box
    gatunek_zwierzaka = Label(root_dodaj_zwierzaka, text=("Gatunek"), font=("Helvetica", 11)).grid(row=2, column=0, sticky=W, padx=5, pady=5)
    gatunek_zwierzaka_box = Entry(root_dodaj_zwierzaka)
    gatunek_zwierzaka_box.grid(row=2, column=1)

    global rasa_zwierzaka_box
    rasa_zwierzaka = Label(root_dodaj_zwierzaka, text=("Rasa"), font=("Helvetica", 11)).grid(row=3, column=0, sticky=W, padx=5, pady=5)
    rasa_zwierzaka_box = Entry(root_dodaj_zwierzaka)
    rasa_zwierzaka_box.grid(row=3, column=1)

    global wiek_zwierzaka_box
    wiek_zwierzaka = Label(root_dodaj_zwierzaka, text=("Wiek"), font=("Helvetica", 11)).grid(row=4, column=0, sticky=W, padx=5, pady=5)
    wiek_zwierzaka_box = Entry(root_dodaj_zwierzaka)
    wiek_zwierzaka_box.grid(row=4, column=1)

    global waga_zwierzaka_box
    waga_zwierzaka = Label(root_dodaj_zwierzaka, text=("Waga"), font=("Helvetica", 11)).grid(row=5, column=0, sticky=W, padx=5, pady=5)
    waga_zwierzaka_box = Entry(root_dodaj_zwierzaka)
    waga_zwierzaka_box.grid(row=5, column=1)

    global pesel_wlasciciela_box
    pesel_wlasciciela = Label(root_dodaj_zwierzaka, text=("Pesel właściciela"), font=("Helvetica", 11)).grid(row=6, column=0, sticky=W, padx=5, pady=5)
    pesel_wlasciciela_box = Entry(root_dodaj_zwierzaka)
    pesel_wlasciciela_box.grid(row=6, column=1)

    dodaj_zwierzaka_button2 = Button(root_dodaj_zwierzaka, text=("Dodaj zwierzaka"), font=("Helvetica", 11), command=lambda: dodaj_zwierzaka2(
        imie_zwierzak_box,gatunek_zwierzaka_box,rasa_zwierzaka_box,wiek_zwierzaka_box,waga_zwierzaka_box,pesel_wlasciciela_box)).grid(row=7, column=0, sticky=W, padx=5, pady=5)

def dodaj_zwierzaka2(imie_zwierzaka,gatunek_zwierzaka,rasa_zwierzaka,wiek_zwierzaka,waga_zwierzaka,pesel_wlasciciela):
    imie_zwierzaka = imie_zwierzak_box.get()
    gatunek_zwierzaka = gatunek_zwierzaka_box.get()
    rasa_zwierzaka = rasa_zwierzaka_box.get()
    wiek_zwierzaka = wiek_zwierzaka_box.get()
    waga_zwierzaka = waga_zwierzaka_box.get()
    pesel_wlasciciela = pesel_wlasciciela_box.get()
    cur.execute("SELECT id_klienta FROM klienci WHERE pesel = ?", (pesel_wlasciciela,))
    id_klienta = cur.fetchone()[0]
    cur.execute("INSERT INTO zwierzaki VALUES(NULL,?,?,?,?,?,?);",(imie_zwierzaka,gatunek_zwierzaka,rasa_zwierzaka,wiek_zwierzaka,waga_zwierzaka,id_klienta))
    Label(root_dodaj_zwierzaka, text="Dodano zwierzaka").grid(row=0, column=2)
    con.commit()
    imie_zwierzak_box.delete(0, END)
    gatunek_zwierzaka_box.delete(0, END)
    rasa_zwierzaka_box.delete(0, END)
    wiek_zwierzaka_box.delete(0, END)
    waga_zwierzaka_box.delete(0, END)
    pesel_wlasciciela_box.delete(0, END)

def wyswietl_zwierzaka():
    root_zwierzaki = Tk()
    root_zwierzaki.title("Lista zwierzaków")
    root_zwierzaki.iconbitmap("img/server.ico")
    root_zwierzaki.geometry("800x600")
    id_zwierzaka = cur.execute("SELECT id_zwierzaka FROM zwierzaki")
    id_zwierzaka = cur.fetchone()
    if id_zwierzaka == None:
        Label(root_zwierzaki, text="Nie ma zwierzaków").grid(row=1, column=0)
    else:
        cur.execute("SELECT * FROM zwierzaki")
        baza = cur.fetchall()
        Label(root_zwierzaki, text="ID", borderwidth=2, relief="groove", width=15).grid(row=0, column=0)
        Label(root_zwierzaki, text="IMIE", borderwidth=2, relief="groove", width=15).grid(row=0, column=1)
        Label(root_zwierzaki, text="GATUNEK", borderwidth=2, relief="groove", width=15).grid(row=0, column=2)
        Label(root_zwierzaki, text="RASA", borderwidth=2, relief="groove", width=15).grid(row=0, column=3)
        Label(root_zwierzaki, text="WIEK", borderwidth=2, relief="groove", width=15).grid(row=0, column=4)
        Label(root_zwierzaki, text="WAGA", borderwidth=2, relief="groove", width=15).grid(row=0, column=5)
        Label(root_zwierzaki, text="ID_WŁAŚCICIELA", borderwidth=2, relief="groove", width=15).grid(row=0, column=6)
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_zwierzaki, text=y, borderwidth=2, relief="groove", width=15)
                dane_label.grid(row=index + 2, column=num)
                num += 1

def wyswietl_baze():
    root_baza = Tk()
    root_baza.title("Baza")
    root_baza.iconbitmap("img/server.ico")
    root_baza.geometry("1700x600")
    id_klienta = cur.execute("SELECT id_klienta FROM klienci")
    id_klienta = cur.fetchone()
    if id_klienta == None:
        Label(root_baza, text="Brak danych w bazie").grid(row=1, column=0)
    else:
        cur.execute("SELECT * FROM klienci AS k INNER JOIN zwierzaki as z ON k.id_klienta = z.id_klienta")
        baza = cur.fetchall()
        Label(root_baza, text="ID KLIENTA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=0, sticky=W)
        Label(root_baza, text="IMIE KLIENTA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=1, sticky=W)
        Label(root_baza, text="NAZWISKO KLIENTA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=2, sticky=W)
        Label(root_baza, text="NUMER TELEFONU KLIENTA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=3, sticky=W)
        Label(root_baza, text="PESEL KLIENTA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=4, sticky=W)
        Label(root_baza, text="ID ZWIERZAKA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=5, sticky=W)
        Label(root_baza, text="IMIE ZWIERZAKA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=6, sticky=W)
        Label(root_baza, text="GATUNEK ZWIERZAKA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=7, sticky=W)
        Label(root_baza, text="RASA ZWIERZAKA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=8, sticky=W)
        Label(root_baza, text="WIEK ZWIERZAKA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=9, sticky=W)
        Label(root_baza, text="WAGA ZWIERZAKA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=10, sticky=W)
        Label(root_baza, text="ID_WŁAŚCICIELA ZWIERZAKA", borderwidth=2, relief="groove", width=22, font=("Helvetica", 7)).grid(row=0, column=11, sticky=W)
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_baza, text=y, borderwidth=2, relief="groove", width=22, font=("Helvetica", 7))
                dane_label.grid(row=index + 2, column=num, sticky=W)
                num += 1

def dodaj_wizyte():
    global root_wizyta
    root_wizyta = Tk()
    root_wizyta.title("Dodaj wizyte")
    root_wizyta.iconbitmap("img/server.ico")
    root_wizyta.geometry("800x600")
    Label(root_wizyta, text="Dodaj wizyte", font=("Helvetica", 16)).grid(row=0, column=0)

    global imie_wlasciciela_box
    imie_wlasciciela = Label(root_wizyta, text=("Imie własciciela"), font=("Helvetica", 11)).grid(row=1, column=0, sticky=W, padx=10)
    imie_wlasciciela_box = Entry(root_wizyta)
    imie_wlasciciela_box.grid(row=1, column=1)
    global nazwisko_wlasciciela_box
    nazwisko_wlasciciela = Label(root_wizyta, text=("Nazwisko właściciela"), font=("Helvetica", 11)).grid(row=2, column=0, sticky=W, padx=10)
    nazwisko_wlasciciela_box = Entry(root_wizyta)
    nazwisko_wlasciciela_box.grid(row=2, column=1)
    global imie_zwierzaka_box
    imie_zwierzaka = Label(root_wizyta, text=("Imie zwierzaka"), font=("Helvetica", 11)).grid(row=3, column=0, sticky=W, padx=10)
    imie_zwierzaka_box = Entry(root_wizyta)
    imie_zwierzaka_box.grid(row=3, column=1)
    global data_wizyty_box
    data_wizyty = Label(root_wizyta, text=("Data wizyty"), font=("Helvetica", 11)).grid(row=4, column=0, sticky=W,padx=10)
    data_wizyty_box = Entry(root_wizyta)
    data_wizyty_box.grid(row=4, column=1)
    global rodzaj_wizyty_box
    rodzaj_wizyty = Label(root_wizyta, text=("Rodzaj wizyty"), font=("Helvetica", 11)).grid(row=5, column=0, sticky=W,padx=10)
    rodzaj_wizyty_box = Entry(root_wizyta)
    rodzaj_wizyty_box.grid(row=5, column=1)

    dodaj_wizyte_button2 = Button(root_wizyta, text='Dodaj wizyte', font=("Helvetica", 10), command=lambda: dodaj_wizyte2(imie_wlasciciela_box,nazwisko_wlasciciela_box,imie_zwierzaka_box,data_wizyty_box,rodzaj_wizyty_box)).grid(row=6, column=0,pady=5,padx=10,sticky=W)

def dodaj_wizyte2(imie_wlasciciela_box,nazwisko_wlasciciela_box,imie_zwierzaka_box,data_wizyty_box,rodzaj_wizyty_box):
    imie_wlasciciela = imie_wlasciciela_box.get()
    nazwisko_wlasciciela = nazwisko_wlasciciela_box.get()
    imie_zwierzaka = imie_zwierzaka_box.get()
    data_wizyty = data_wizyty_box.get()
    rodzaj_wizyty = rodzaj_wizyty_box.get()
    cur.execute("INSERT INTO wizyty VALUES(NULL,?,?,?,?,?);",(imie_wlasciciela, nazwisko_wlasciciela, imie_zwierzaka, data_wizyty, rodzaj_wizyty))
    Label(root_wizyta, text="Dodano wizyte").grid(row=0, column=2)
    con.commit()
    imie_wlasciciela_box.delete(0, END)
    nazwisko_wlasciciela_box.delete(0, END)
    imie_zwierzaka_box.delete(0, END)
    data_wizyty_box.delete(0, END)
    rodzaj_wizyty_box.delete(0, END)

def wyswietl_wizyty():
    root_wywietl_zwierzaka = Tk()
    root_wywietl_zwierzaka.title("Lista wizyt")
    root_wywietl_zwierzaka.iconbitmap("img/server.ico")
    root_wywietl_zwierzaka.geometry("900x600")
    id_wizyty = cur.execute("SELECT id_wizyty FROM wizyty")
    id_wizyty = cur.fetchone()
    if id_wizyty == None:
        Label(root_wywietl_zwierzaka, text="Nie ma wizyt").grid(row=1, column=0)
    else:
        cur.execute("SELECT * FROM wizyty")
        baza = cur.fetchall()
        Label(root_wywietl_zwierzaka, text="ID WIZYTY", borderwidth=2, relief="groove", width=20).grid(row=0, column=0)
        Label(root_wywietl_zwierzaka, text="IMIE WŁAŚCICIELA", borderwidth=2, relief="groove", width=20).grid(row=0, column=1)
        Label(root_wywietl_zwierzaka, text="NAZWISKO WŁAŚCICIELA", borderwidth=2, relief="groove", width=20).grid(row=0, column=2)
        Label(root_wywietl_zwierzaka, text="IMIE ZWIERZAKA", borderwidth=2, relief="groove", width=20).grid(row=0, column=3)
        Label(root_wywietl_zwierzaka, text="DATA WIZYTY", borderwidth=2, relief="groove", width=20).grid(row=0, column=4)
        Label(root_wywietl_zwierzaka, text="RODZAJ WIZYTY", borderwidth=2, relief="groove", width=20).grid(row=0, column=5)
        for index, x in enumerate(baza):
            num = 0
            for y in x:
                dane_label = Label(root_wywietl_zwierzaka, text=y, borderwidth=2, relief="groove", width=20)
                dane_label.grid(row=index + 2, column=num)
                num += 1


imie_klienta = Label(root, text=("Imie"), font=("Helvetica", 11)).grid(row=1, column=0, sticky=W, padx=10)
imie_klienta_box = Entry(root)
imie_klienta_box.grid(row=1, column=1)

nazwisko_klienta = Label(root, text=("Nazwisko"), font=("Helvetica", 11)).grid(row=2, column=0, sticky=W, padx=10)
nazwisko_klienta_box = Entry(root)
nazwisko_klienta_box.grid(row=2, column=1, pady=5)

nr_tel_klienta = Label(root, text=("Numer telefonu"), font=("Helvetica", 11)).grid(row=3, column=0, sticky=W, padx=10)
nr_tel_klienta_box = Entry(root)
nr_tel_klienta_box.grid(row=3, column=1, pady=5)

pesel_klienta = Label(root, text=("Pesel"), font=("Helvetica", 11)).grid(row=4, column=0, sticky=W, padx=10)
pesel_klienta_box = Entry(root)
pesel_klienta_box.grid(row=4, column=1, pady=5)

dodaj_klienta_button = Button(root, text='Dodaj klienta', font=("Helvetica", 10), command=lambda: dodaj_klienta(imie_klienta_box,nazwisko_klienta_box,nr_tel_klienta_box,pesel_klienta_box)).grid(row=5, column=0, pady=5, padx=5, sticky=W)
dodaj_zwierzaka = Button(root, text='Dodaj zwierzaka', font=("Helvetica", 10), command=dodaj_zwierzaka).grid(row=5, column=1, padx=5, pady=5, sticky=W)
dodaj_wizyte_button = Button(root, text='Dodaj wizyte', font=("Helvetica", 10), command=dodaj_wizyte).grid(row=5, column=2, padx=5, pady=5, sticky=W)
wyswietl_klienta_button = Button(root, text='Wyświetl klientów', font=("Helvetica", 10), command= wyswiel_klienci).grid(row=6, column=0, padx=5, pady=5, sticky=W)
#edytuj_klienta_button = Button(root, text='Edytuj klienta', font=("Helvetica", 10), command=edytuj_klienta).grid(row=5, column=1, padx=5, pady=5, sticky=W)
wyszukaj_klienta_button = Button(root, text='Wyszukaj klienta', font=("Helvetica", 10), command=wyszukaj_klienta).grid(row=6, column=1, padx=5, pady=5, sticky=W)
wyswietl_zwierzaka_button = Button(root, text='Wyświetl zwierzaki', font=("Helvetica", 10), command=wyswietl_zwierzaka).grid(row=6, column=2, padx=5, pady=5, sticky=W)
wyswietl_wizyte_button = Button(root, text='Wyświetl wizyty', font=("Helvetica", 10), command=wyswietl_wizyty).grid(row=7, column=0, padx=5, pady=5, sticky=W)
wyswietl_baze_button = Button(root, text='Wyświetl baze', font=("Helvetica", 10), command=wyswietl_baze).grid(row=7, column=1, padx=5, pady=5, sticky=W)

root.mainloop()