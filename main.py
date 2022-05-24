class Biblioteka:
    lista_ksiazek = []
    lista_egzemplarzy = []
    lista_czytelnikow = []

    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen = limit_wypozyczen

    def dodaj_egzemplarz_ksiazki(self, ksiazka):
            self.lista_ksiazek.append(ksiazka)
            return True
    
    def wypozycz(self, czytelnik, tytul):
        if len(czytelnik.lista_czytelnika) < 3:
            for ksiazka in self.lista_ksiazek:
                if ksiazka.tytul == tytul:
                    for ksiazka_czytelnika in czytelnik.lista_czytelnika:
                        if ksiazka_czytelnika.tytul == tytul:
                            return False
                    czytelnik.lista_czytelnika.append(ksiazka)
                    self.lista_ksiazek.remove(ksiazka)
                    return True
        return False

    def oddaj(self, nazwisko, tytul):
        for czytelnik in self.lista_czytelnikow:
            if czytelnik.nazwisko == nazwisko:
                for ksiazka_czytelnika in czytelnik.lista_czytelnika:
                    if ksiazka_czytelnika.tytul == tytul:
                        self.lista_ksiazek.append(ksiazka_czytelnika)
                        return True
        return False 
    

class Ksiazka:

    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

class Egzemplarz:

    def __init__(self, rok_wydania, wypozyczony):
        self.rok_wydania = rok_wydania
        self.wypozyczony = wypozyczony

class Czytelnik:

    def __init__(self, nazwisko, tytul):
        self.nazwisko = nazwisko
        self.tytul = tytul


biblioteka = Biblioteka(25)
n = int(input())
lista_akcji = [eval(input().strip()) for akcja in range(n)]

for akcja in lista_akcji:
    if akcja[0].strip() == 'dodaj':
        ksiazka = Ksiazka(tytul=akcja[1].strip(), autor=akcja[2].strip(), rok=akcja[3])
        print(biblioteka.dodaj_egzemplarz_ksiazki(ksiazka))
    elif akcja[0].strip() == 'wypozycz': 
        czytelnik_w_bazie = False
        tytul = akcja[2].strip()
        for czytelnik in biblioteka.lista_czytelnikow:
            if czytelnik.nazwisko == akcja[1].strip():
                print(biblioteka.wypozycz(czytelnik, tytul))
                break
            if not czytelnik_w_bazie:
                czytelnik_nowy = Czytelnik(akcja[1].strip(), [])
                biblioteka.lista_czytelnikow.append(czytelnik_nowy)
    elif akcja[0].strip() == 'oddaj':
        nazwisko = akcja[1].strip()
        tytul = akcja[2].strip()
        print(biblioteka.oddaj(nazwisko, tytul))


    
