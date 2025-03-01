# Task description available in README.md

from faker import Faker
fake = Faker()


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_number}, {self.email}"

    def contact(self):
        return f"I dial number {self.phone_number} and call {self.first_name} {self.last_name}."

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name) + 1


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


# function that create Base and Business Cards according to user input
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


if __name__ == "__main__":
    # variables to let the user decide how many and what type of cards system should create
    base_contact_qty = int(input("How many Base Contact cards should be created? Enter an integer number:"))
    business_contact_qty = int(input("How many Business Contact cards should be created? Enter an integer number:"))

    contacts = create_contacts("P", base_contact_qty) + create_contacts("B", business_contact_qty)

    # sorting business card per attribute
    by_first_name = sorted(contacts, key=lambda card3: card3.first_name)
    by_last_name = sorted(contacts, key=lambda card3: card3.last_name)
    by_email = sorted(contacts, key=lambda card3: card3.email)

    # print contacts
    print("\n===========Create Contact Cards==========")
    for contact in contacts:
        print(contact)
