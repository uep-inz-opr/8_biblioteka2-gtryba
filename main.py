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

    def __init__(self, nazwisko, lista_czytelnika):
        self.nazwisko = nazwisko
        self.lista_czytelnika = lista_czytelnika


biblioteka = Biblioteka(25)
n = int(input())
lista_akcji = [input().strip(' ') for akcja in range(n)]
usuwanie = []

for x in lista_akcji:
        usun_nawias = x.replace("(", "")
        usun_nawias2 = usun_nawias.replace(")", "")
        usun_cudzyslow = usun_nawias2.replace("\"", "")
        usuwanie = usun_cudzyslow.split(", ")
        if usuwanie[0].strip() == "dodaj":
            ksiazka = Ksiazka(tytul=usuwanie[1].strip(), autor=usuwanie[2].strip(), rok=usuwanie[3].strip())
            print(biblioteka.dodaj_egzemplarz_ksiazki(ksiazka))
        if usuwanie[0].strip() == "wypozycz":
            jest_czytelnik = False
            tytul = usuwanie[2].strip()
            for czytelnik in biblioteka.lista_czytelnikow:
                if czytelnik.nazwisko == usuwanie[1].strip():
                    jest_czytelnik = True
                    print(biblioteka.wypozycz(czytelnik, tytul))
                    break
            if not jest_czytelnik:
                nowy = Czytelnik(usuwanie[1].strip(), [])
                biblioteka.lista_czytelnikow.append(nowy)
                print(biblioteka.wypozycz(nowy, tytul))
        if usuwanie[0].strip() == "oddaj":
            nazwisko = usuwanie[1].strip()
            tytul = usuwanie[2].strip()
            print(biblioteka.oddaj(nazwisko, tytul))

    
