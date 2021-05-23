import json
from Contact import Contact

class PhoneBook:
    def read_from_file(self):
        contacts_file = open('contacts.json')
        contact_dicts = json.load(contacts_file)
        contacts = []

        for dict in contact_dicts:
            contacts.append(Contact.from_json(dict))

        return contacts

    def show_list(self):
        contacts = self.read_from_file()

        for contact in contacts:
            print(f"{contact.id}     {contact.firstname} {contact.lastname}")