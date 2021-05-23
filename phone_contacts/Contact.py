from datetime import date

class Contact:
    id = 0
    firstname = ''
    lastname = ''
    phone_number = ''
    company = ''
    date_of_birth = None
    blocked = False

    def __init__(self, firstname, lastname, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number

    def from_json(dict):
        contact = Contact(dict['firstname'], dict['lastname'], dict['phone_number'])
        contact.id = dict['id']
        return contact