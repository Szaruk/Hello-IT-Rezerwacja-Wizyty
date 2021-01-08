import sqlite3

con = sqlite3.connect('przychodnia.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS klienci(
        id_klienta INTEGER NOT NULL PRIMARY KEY,
        imie varchar(45) NOT NULL,
        nazwisko varchar(45) NOT NULL,
        numer_tel varchar(9) NOT NULL,
        pesel varchar(11) NOT NULL
)""")

cur.executescript("""
    CREATE TABLE IF NOT EXISTS zwierzaki(
        id_zwierzaka INTEGER NOT NULL PRIMARY KEY,
        imie VARCHAR(45),
        gatunek VARCHAR(45),
        rasa VARCHAR(45),
        wiek VARCHAR(2),
        waga VARCHAR(2),
        id_klienta INTEGER NOT NULL,
        FOREIGN KEY(id_klienta) REFERENCES klienci(id)
)""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS wizyty(
        id_wizyty INTEGER NOT NULL PRIMARY KEY,
        imie_wlaciciela VARCHAR(45),
        nazwisko_wlaciciela VARCHAR(45),
        imie_zwierzaka VARCHAR(45),
        data_wizyty VARCHAR(45),
        rodzaj_wizyty VARCHAR(45)
)""")
