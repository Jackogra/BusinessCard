# Task description available in README.md

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


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.label_length = len(self.first_name) + len(self.last_name)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_number}, {self.email}"

    def contact(self):
        return f"I dial number {self.phone_number} and call {self.first_name} {self.last_name}."


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone_number, email, job, company, work_phone):
        super().__init__(first_name, last_name, phone_number, email)
        self.job = job
        self.company = company
        self.work_phone = work_phone

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.job}, {self.company}, {self.work_phone}, {self.email}"

    def contact(self):
        return f"I dial number {self.work_phone} and call {self.first_name} {self.last_name}."


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

base_data = [
    BaseContact(fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email()) for i in range(5)]


business_data = [
    BusinessContact(fake.first_name(),
                    fake.last_name(),
                    fake.phone_number(),
                    fake.email(),
                    fake.company(),
                    fake.job(),
                    fake.phone_number()) for k in range(5)]

# print out Base Contact information
print("\n===========Base Contact output:==========")
for data in base_data:
    print(data.contact())

# print out Business Contact information
print("\n==========Business Contact output:==========")
for data in business_data:
    print(data.contact())

# print Base Contact name lengths
print("\n==========BaseContact Name and it's length===========")
for basename in base_data:
    print(f"Name: {basename.first_name} {basename.last_name} - Length: {basename.label_length}")

# print Business Contact name lengths
print("\n==========BusinessContact Name and it's length===========")
for businessname in business_data:
    print(f"Name: {businessname.first_name} {businessname.last_name} - Length: {businessname.label_length}")


def create_contacts(contact_type, quantity):
    contacts = []

    for i in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email = fake.email()

        if contact_type == "P":
            contact = BaseContact(first_name, last_name, phone_number, email)
        elif contact_type == "B":
            job = fake.job()
            company = fake.company()
            work_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, phone_number, email, job, company, work_phone)
        else:
            return "Invalid contact type! Type 'P' for Base (Personal) Card or 'B' for Business Card."

        contacts.append(contact)

    return contacts


base_cards = create_contacts("P", 5)
business_cards = create_contacts("B", 5)

# print Cards with create contacts function
print("\n===========Create Base Contact Cards==========")
for contact in base_cards:
    print(contact)

print("\n===========Create Business Contact Cards==========")
for contact in business_cards:
    print(contact)
