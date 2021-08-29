import json
from Contact import Contact

class PhoneBook:
    selected_contact_id = 0

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
        elif selection == '2':
            self.show_search()
        elif selection == '3':
            self.show_list()
        else:
            print('Please select option 1, 2 or 3')

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

    def show_search(self):
        keyword = input('Search: ').lower()
        contacts = self.read_from_file()
        filtered = []

        for contact in contacts:
            first_name = contact.firstname.lower()
            last_name = contact.lastname.lower()
            phone_number = contact.phone_number

            if first_name.find(keyword) >= 0 or last_name.find(keyword) >= 0 or phone_number.find(keyword) >= 0:
                filtered.append(contact)

        if len(filtered) > 0:
            self.print_contacts(filtered)
            self.show_list_options()
        else:
            print('No contacts found.')

    def show_list(self):
        contacts = self.read_from_file()
        self.print_contacts(contacts)
        self.show_list_options()

    def print_contacts(self, contacts):
        for contact in contacts:
            print(f"{contact.id}     {contact.firstname} {contact.lastname}")

    def show_list_options(self):
        print('[1] Select    [2] Main Menu')
        selection = input()

        if selection == '1':
            self.select()
        elif selection == '2':
            self.show_start_menu()

    def select(self):
        self.selected_contact_id = int(input('ID: '))
        self.show_contact()

    def show_contact(self):
        contact = self.find_by_id(self.selected_contact_id)

        if contact != None:
            print(f"Name: {contact.firstname} {contact.lastname}")
            print(f"Phone number: {contact.phone_number}")
            print(f"Company: {contact.company}")

            if (contact.date_of_birth != None):
                print(f"Date of Birth: {contact.date_of_birth.strftime('%d.%m.%Y')}")

            if (contact.blocked):
                print('Blocked: Yes')
            else:
                print('Blocked: No')
            

    def find_by_id(self, id):
        contacts = self.read_from_file()

        for contact in contacts:
            if contact.id == id:
                return contact

        return None