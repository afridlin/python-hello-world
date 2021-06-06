import json
from Contact import Contact

class PhoneBook:
    def read_from_file(self):
        contacts_file = open('contacts.json', 'r')
        contact_dicts = json.load(contacts_file)
        contacts = []

        for dict in contact_dicts:
            contacts.append(Contact.from_json(dict))

        contacts_file.close()
        return contacts

    def save_to_file(self, contacts):
        contacts_file = open('contacts.json', 'w')
        dicts = []

        for contact in contacts:
            dicts.append(contact.to_json())

        json.dump(dicts, contacts_file)
        contacts_file.close()

    def show_start_menu(self):
        print('[1] Add \n[2] Search \n[3] List')
        selection = input()
        
        if selection == '1':
            self.show_add_dialog()

    def show_add_dialog(self):
        first_name = input('First name: ')
        last_name = input('Last name: ')
        phone_number = input('Phone number: ')

        contact = Contact(first_name, last_name, phone_number)
        self.insert_contact(contact)

    def insert_contact(self, contact):
        contacts = self.read_from_file()
        contact.id = len(contacts) + 1
        contacts.append(contact)
        self.save_to_file(contacts)

    def show_list(self):
        contacts = self.read_from_file()

        for contact in contacts:
            print(f"{contact.id}     {contact.firstname} {contact.lastname}")