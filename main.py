class Biblioteka:
    lista_ksiazek = []
    lista_egzemplarzy = []
    lista_krotek = []
    lista_ostateczna = []
    lista_czytelnikow = []
    czy_jest_w_liscie = False
    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen = limit_wypozyczen

    def sortuj(self, e):
        return e['tytul']

    def dostepne_egzemplarze(self):
        for ksiazka in self.lista_ksiazek:
            for egzemplarze in self.lista_egzemplarzy:
                if egzemplarze.tytul == ksiazka.tytul and egzemplarze.autor == ksiazka.autor:
                    self.czy_jest_w_liscie = True
            if not self.czy_jest_w_liscie:
                self.lista_ostateczna.append({'tytul': ksiazka.tytul, 'autor': ksiazka.autor, 'ilosc_egzemplarzy': self.liczEgzemplarze(ksiazka)})
                self.czy_jest_w_liscie = False
                self.lista_egzemplarzy.append(ksiazka)
            self.czy_jest_w_liscie = False
        self.lista_ostateczna.sort(key=self.sortuj)
        #for lista in self.lista_ostateczna:
            #print("('" + lista['tytul'].strip() + "'" + ", " + "'" + lista['autor'].strip() + "', " + lista['ilosc_egzemplarzy'].strip() + ")")
    def wypozycz(self, nazwisko, tytul):
        czytelnik = Czytelnik(nazwisko, tytul)
        self.lista_czytelnikow.append(czytelnik)

        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                self.lista_ksiazek.remove(ksiazka)
                return True
            else: 
                return False

    def oddaj(self, nazwisko, tytul):
        self.lista_ksiazek.append(tytul) 
        for i in range(len(self.lista_czytelnikow)):
            temp = self.lista_czytelnikow[i]
            if temp.nazwisko == nazwisko and temp.tytul == tytul:
                print(temp.nazwisko, "?")
                self.lista_czytelnikow.remove(self.lista_czytelnikow[i])
                return True
            else:
                return False   
    
    def dodaj_egzemplarz_ksiazki(self, ksiazka):
        self.lista_ksiazek.append(ksiazka)
        return True

    def liczEgzemplarze(self, aktualna_ksiazka):
        wynik = 0
        for ksiazka in self.lista_ksiazek:
            if aktualna_ksiazka.tytul == ksiazka.tytul and aktualna_ksiazka.autor == ksiazka.autor:
                wynik += 1

        return str(wynik)

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
    lista_wypozyczonych_egzemplarzy=[]
    def __init__(self, nazwisko, tytul):
        self.nazwisko = nazwisko
        self.tytul = tytul

    def wypozycz(self, tytul):
        for tytul in self.lista_wypozyczonych_egzemplarzy:
            if tytul not in self.lista_wypozyczonych_egzemplarzy:
                self.lista_wypozyczonych_egzemplarzy.append(tytul)
            else:
                return
        
        



lista_ksiazek = []
biblioteka = Biblioteka(10)

n = int(input())
lista_akcji = [eval(input().strip()) for akcja in range(n)]
print(lista_akcji[0])

for akcja in lista_akcji:
    if akcja[0].strip() == 'dodaj':
        ksiazka = Ksiazka(tytul=akcja[1].strip(), autor=akcja[2].strip(), rok=akcja[3])
        print(biblioteka.dodaj_egzemplarz_ksiazki(ksiazka))
    elif akcja[0].strip() == 'wypozycz': 
        print(biblioteka.wypozycz(akcja[1].strip(), akcja[2].strip()))
    elif akcja[0].strip() == 'oddaj':
        print(biblioteka.oddaj(akcja[1].strip(), akcja[2].strip()))


    
