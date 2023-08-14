def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter name"
    return wrapper

@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return f"Contact {name} with phone {phone} added."

@input_error
def find_contact(contacts, name):
    return contacts[name]

@input_error
def update_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} changed to {phone}."
    else:
        return "Enter name"

def show_contacts(contacts):
    if contacts:
        output = "Your contact book:\n"
        for name, phone in contacts.items():
            output += f"{name} - {phone}\n"
        return output
    else:
        return "Your contact book is empty."

def main():
    contacts = {}

    while True:
        command = input("Enter a command: ").lower()
        words = command.split()
        command_name = words[0]

        if command_name == "hello":
            print("How can I help you?")
        elif command_name == "add":
            try:
                name, phone = words[1], words[2]
                response = add_contact(contacts, name, phone)
                print(response)
            except IndexError:
                print("Give me name and phone please")
        elif command_name == "phone":
            try:
                name = words[1]
                print(find_contact(contacts, name))
            except IndexError:
                print("Enter name")
        elif command_name == "change":
            try:
                name, phone = words[1], words[2]
                response = update_contact(contacts, name, phone)
                print(response)
            except IndexError:
                print("Give me name and phone please")
        elif command_name == "show":
            print(show_contacts(contacts))
        elif command_name in ("good bye", "close", "exit"):
            print("Good bye!")
            break
        else:
            print("Something went wrong. Please try again.")

if __name__ == "__main__":
    main()