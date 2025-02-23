"""
1. Stwórz klasę, która będzie przechowywać informacje z jednej wizytówki.
Przyjmij, że każda wizytówka zawiera dane takie jak: imię, nazwisko, nazwa firmy, stanowisko, adres e-mail. - __DONE

Zdefiniuj listę, która będzie zawierała 5 wizytówek ludzi o losowych danych
(dane możesz skopiować ze strony takiej jak Fake Name Generator. - __DONE

Skonstruuj pętlę, która wyświetli całą zawartość listy wizytówek tak, aby w jednej linii widoczne było imię,
nazwisko i adres e-mail właściciela wizytówki. - __DONE

2. Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę. Używając biblioteki faker,
którą opisaliśmy powyżej. Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja. - __DONE


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
from faker import Faker
fake = Faker()


class BusinessCard:
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}"

    def contact(self):
        return f"I am reaching out to {self.first_name} {self.last_name} - {self.job} - {self.email}"

    @property
    def first_name_len(self):
        return len(self.first_name)

    @property
    def last_name_len(self):
        return len(self.last_name)


# business card list for task 1
business_cards = [
    BusinessCard("Maryann", "Hester", "Realty Zone", "Information clerk", "MaryannHester@rhyta.com"),
    BusinessCard("Idella", "Goddard", "Hill-Behan", "Gerontology social worker", "IdellaGoddard@rhyta.com"),
    BusinessCard("Ella", "Evans", "Integra Wealth Planners", "Applied mathematician", "EllaEvans@jourrapide.com"),
    BusinessCard("Martin", "Lau", "Leath Furniture", "Conference service coordinator", "MartinLau@armyspy.com"),
    BusinessCard("Terry", "Workman", "Northern Reflections", "Upholsterer", "TerryWorkman@armyspy.com"),]

# for loop to display data from the business cards
print("\n==================== Output for task 1: ====================")
for card in business_cards:
    print(card.first_name, card.last_name, "-", card.email)

# creating a list of business cards using faker module
fake_business_card = [
    BusinessCard(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email()) for i in range(5)]

# for loop to display data from the business cards created with faker module
print("\n==================== Output for task 2: ====================")
for fake_card in fake_business_card:
    print(fake_card.first_name, fake_card.last_name, "-", fake_card.company, "-", fake_card.job, "-", fake_card.email)

# for loop to display data for task 3a
print("\n==================== Output for taks 3a: ====================")
for fake_card in fake_business_card:
    print(fake_card)


def __gt__(fake2, other):
    return fake2 > other


# crate a new list for task 3b
sorted_business_cards = [
    BusinessCard(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email()) for i in range(10)]

# sorting business card per attribute
by_first_name = sorted(sorted_business_cards, key=lambda card3: card3.first_name)
by_last_name = sorted(sorted_business_cards, key=lambda card3: card3.last_name)
by_email = sorted(sorted_business_cards, key=lambda card3: card3.email)

# printing output for task 3b
print("\n==================== Output for task 3b: ====================\n--> by first_name:")
for i in by_first_name:
    print(i)

print("\n--> by last_name:")
for i in by_last_name:
    print(i)

print("\n--> by email:")
for i in by_email:
    print(i)

# printing output for task 4a
print("\n==================== Output for task 4a: ====================")
for fake_card in fake_business_card:
    print(fake_card.contact())

# printing output for task 4b
print("\n==================== Output for task 4b: ====================")
for fake_card in fake_business_card:
    print(f"First name length: {fake_card.first_name} - {fake_card.first_name_len}, "
          f"Last name length: {fake_card.last_name} - {fake_card.last_name_len}")
