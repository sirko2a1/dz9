import csv

def check_file():
    try:
        with open('data.txt') as f:
            DATA = list(csv.reader(f))
    except FileNotFoundError:
        with open('data.txt', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'age', 'phone'])
            DATA = []
    return DATA

def add():
    DATA = check_file()
    name = input('Enter name: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    DATA.append([name, age, phone])
    with open('data.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(DATA)
    print('Данні додані!')

def change():
    DATA = check_file()
    index = int(input('Введіть індекс: '))
    name = input('Введіть нове імя: ')
    age = input('Введіть новий вік: ')
    phone = input('Введіть номер: ')
    DATA[index] = [name, age, phone]
    with open('data.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(DATA)
    print('Данні були змінені!')

def search():
    DATA = check_file()
    name = input('Введіть імя: ')
    phone = None
    for row in DATA[1:]:
        if row[0] == name:
            phone = row[2]
            break
    if phone is not None:
        print(f'Телефонний номер {name} це {phone}')
    else:
        print(f'{name} хто це? в нас немає таких')

def show():
    DATA = check_file()
    for row in DATA:
        print(', '.join(row))

def delete():
    DATA = check_file()
    index = int(input('Введіть індекс: '))
    DATA.pop(index)
    with open('data.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(DATA)
    print('Данні видалені!')

commands = {
    'add': add,
    'change': change,
    'search': search,
    'show': show,
    'delete': delete,
}
print('Раді вас вітати в нашому боті!')
print('Ви можете використовувати наступні команди:')
print('add - додати нові данні')
print('change - щоб змінити існуючі дані')
print('search - щоб знайти номер телефона за імям')
print('show - показати усі данні')
print('delete - щоб видалити існуючі данні')
print('exit - щоб вийти з програми')

while True:
    command = input('Введіть команду: ')
    if command in commands:
        commands[command]()
    elif command == 'exit':
        print('Бувайте здорові!')
        break
    else:
        print('Щось не так')
