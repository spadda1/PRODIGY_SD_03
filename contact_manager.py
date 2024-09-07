import json

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def edit_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            self.save_contacts()
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
        else:
            print("Contact not found.")
