import json

CONTACTS_FILE = "contacts.json"

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def save_contacts(self):
        with open(CONTACTS_FILE, "w") as f:
            json.dump(self.contacts, f)

    def load_contacts(self):
        try:
            with open(CONTACTS_FILE, "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            pass

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        self.save_contacts()

    def find_contact(self, name):
        return self.contacts.get(name, "Enter user name.")

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            self.save_contacts()
        else:
            return "Enter user name."

    def show_contacts(self):
        if self.contacts:
            output = "Your contact book:\n"
            for name, phone in self.contacts.items():
                output += f"{name} - {phone}\n"
            return output
        else:
            return "Your contact book is empty."

def main():
    contact_book = ContactBook()

    while True:
        command = input("Enter a command: ").lower()
        words = command.split()
        command_name = words[0]

        if command_name == "hello":
            print("How can I help you?")
        elif command_name == "add":
            name, phone = words[1], words[2]
            contact_book.add_contact(name, phone)
            print(f"Contact {name} with phone {phone} added.")
        elif command_name == "phone":
            name = words[1]
            print(contact_book.find_contact(name))
        elif command_name == "change":
            name, phone = words[1], words[2]
            result = contact_book.update_contact(name, phone)
            if result:
                print(result)
            else:
                print(f"Contact {name} updated with phone {phone}.")
        elif command_name == "show":
            print(contact_book.show_contacts())
        elif command_name in ("good bye", "close", "exit"):
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
