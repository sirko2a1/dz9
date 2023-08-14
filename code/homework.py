import json

CONTACTS_FILE = "contacts.json"

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            return {}
    return wrapper

@error_handler
def load_contacts():
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f)

def add_contact(contacts, name, phone):
    contacts[name] = phone
    save_contacts(contacts)

def find_contact(contacts, name):
    return contacts.get(name, "Введіть username.")

def update_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        save_contacts(contacts)
    else:
        return "Введіть username."

def show_contacts(contacts):
    if contacts:
        output = "Ваша контактна книга:\n"
        for name, phone in contacts.items():
            output += f"{name} - {phone}\n"
        return output
    else:
        return "Ваша контактна книга пуста."

def main():
    contacts = load_contacts()

    while True:
        command = input("Введіть команду: ").lower()
        words = command.split()
        command_name = words[0]

        if command_name == "hello":
            print("Чим я можу допомогти?")
        elif command_name == "add":
            name, phone = words[1], words[2]
            add_contact(contacts, name, phone)
            print(f"Контакт {name} з номером {phone} додано.")
        elif command_name == "phone":
            name = words[1]
            print(find_contact(contacts, name))
        elif command_name == "change":
            name, phone = words[1], words[2]
            result = update_contact(contacts, name, phone)
            if result:
                print(result)
            else:
                print(f"Контакт {name} змінено на {phone}.")
        elif command_name == "show":
            print(show_contacts(contacts))
        elif command_name in ("good bye", "close", "exit"):
            print("Бувайте здорові!")
            break
        else:
            print("Щось не так. Спробуйте знов.")

if __name__ == "__main__":
    main()
