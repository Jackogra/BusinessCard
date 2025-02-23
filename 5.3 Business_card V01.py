"""
1. Wyobraź sobie, że właśnie wracasz z obchodów Dni Sapera (niezwykle hucznych),
Święta Bigosu, albo Konwencji Wielbicieli Pizzy Hawajskiej. Jedno jest pewne
– masz całą kolekcję wizytówek od ludzi, z którymi chcesz utrzymać kontakt
przydałaby się książka adresowa, żeby ich wszystkich nie pogubić.

Stwórz klasę, która będzie przechowywać informacje z jednej wizytówki.
Przyjmij, że każda wizytówka zawiera dane takie jak: imię, nazwisko, nazwa firmy, stanowisko, adres e-mail.

Zdefiniuj listę, która będzie zawierała 5 wizytówek ludzi o losowych danych
(dane możesz skopiować ze strony takiej jak Fake Name Generator.

Skonstruuj pętlę, która wyświetli całą zawartość listy wizytówek tak, aby w jednej linii widoczne było imię,
nazwisko i adres e-mail właściciela wizytówki.


2. Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę. Używając biblioteki faker,
którą opisaliśmy powyżej. Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja.


3a. Zmodyfikuj kod z poprzedniego ćwiczenia na temat książki adresowej tak, aby obiekt wizytówki
przedstawiony jako string zawierał imię, nazwisko i adres e-mail osoby, do której należy wizytówka.

3b. Stwórz listę wizytówek, a następnie używając funkcji sorted(), ułóż ją na trzy sposoby
– według imienia, nazwiska oraz adresu e-mail.


4a. Rozwiń program przechowujący wizytówki. Do klasy opisującej wizytówkę dodaj metodę contact(),
która wypisze na konsoli napis “Kontaktuję się z …”, a na końcu wyświetli imię, nazwisko,
stanowisko i adres e-mail osoby, z którą chcemy się skontaktować.

4b. W klasie przechowującej wizytówkę zdefiniuj dynamiczny atrybut (używając @property),
który będzie zwracał sumę długości imienia i nazwiska oddzielonych spacją. Tę informację można wykorzystać
przykładowo przy adresowaniu kopert lub zaproszeń, gdzie często miejsce na imię i nazwisko jest dosyć ograniczone.


5a. Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna
przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy
(BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko,
nazwa firmy, telefon służbowy.

5b. Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci
“Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu,
a wizytówka bazowa prywatny.

5c. Oba typy wizytówek powinny mieć dynamiczny atrybut label_length,
który zwraca długość imienia i nazwiska danej osoby.

5d. Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki.
Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość.
Wykorzystaj bibliotekę faker do generowania danych.
"""


class BusinessCard:
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email
