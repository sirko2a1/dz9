def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Введіть username'
        except ValueError:
            return 'Дайте мені імя та телефон'
        except IndexError:
            return 'Введіть команду'
    return inner

@input_error
def hello_handler(*args):
    return 'Чим я можу допомогти?'

@input_error
def add_handler(*args):
    if len(args) != 2:
        return 'Дайте мені імя та телефон'
    name, phone = args
    contacts[name] = phone
    return f'Контакт {name} з телефоном {phone} додано!'

@input_error
def change_handler(*args):
    if len(args) != 2:
        return 'Дайте мені імя та телефон'
    name, phone = args
    if name not in contacts:
        return 'Контакт не знайдено('
    contacts[name] = phone
    return f'Контакт {name} змінено!'

@input_error
def phone_handler(*args):
    if len(args) != 1:
        return 'Введіть username'
    name = args[0]
    return contacts[name]

@input_error
def show_all_handler(*args):
    result = ''
    for name, phone in contacts.items():
        result += f'{name}: {phone}\n'
    return result

def main():
    while True:
        command = input('Введіть команду: ').lower()
        if command == 'hello':
            print(hello_handler())
        elif command == 'add':
            print(add_handler(*input('Дайте мені імя та телефон: ').split()))
        elif command == 'change':
            print(change_handler(*input('Дайте мені імя та телефон: ').split()))
        elif command == 'phone':
            print(phone_handler(*input('Введіть імя: ').split()))
        elif command == 'show all':
            print(show_all_handler())
        elif command in ('good bye', 'close', 'exit'):
            print('Дай вам боже здоровячка, заходіть ще!')
            break
        else:
            print('Щось не так!')

contacts = {}
main()
