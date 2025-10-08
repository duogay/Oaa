import re

import commandRun as cr
from dataBase import Table

db = {}

def start_session():
    print('Очікую команду...')

    while True:
        command = ''

        while ';' not in command:
            command = command + input() + ' '

        command = command.split(';')[0]
        command = command.strip().split()
        command = ' '.join(command)
            
        match command:
            case create if create.lower().startswith('create'):
                if command.count(' ') == 0:
                    print('Відсутні аргументи після CREATE.')
                    continue
                    
                command = re.sub('create ', '', command, 1)

                try:
                    table_name, data = command.split('(', maxsplit=1)
                    if data[-1] == ')':
                        data = data.rstrip()[:-1]
                    else:
                        print('")" не існує в кінці аргументів')
                        continue
                except ValueError:
                    print('Відсутня "(" для позначення початку аргументів.')
                    continue
                except IndexError:
                    print('Не існує значень column_name та ")".')
                    continue
                        
                table_name = table_name.strip()

                data = data.split(',')
                for i in range(len(data)):
                    data[i] = data[i].strip()

                if cr.createTable(table_name, data):
                    if table_name in db:
                        print(f'Неможливо створити таблицю {table_name}, таблиця з такою назвою вже існує.')
                    else:
                        db[table_name] = Table(data)
                        print(f'Таблиця {table_name} Була створена.')

            case insert if insert.lower().startswith('insert'):
                if command.lower().startswith('insert into'):
                    command = re.sub(' into', '', command, 1)

                if command.count(' ') == 0:
                    print('Відсутні аргументи після INSERT [INTO].')
                    continue
                    
                command = re.sub('insert ', '', command, 1)
                try:
                    table_name, data = command.split('(', maxsplit=1)
                    if data.rstrip()[-1] == ')':
                        data = data.rstrip()[:-1]
                    else:
                        print('")" не існує в кінці аргументів')
                        continue
                except ValueError:
                    print('Відсутня "(" для позначення початку аргументів.')
                    continue
                except IndexError:
                    print('Не існує значень "value" та ")".')
                    continue
                    
                table_name = table_name.strip()

                data = data.split(',')
                for i in range(len(data)):
                        data[i] = data[i].strip()

                if cr.insertInto(table_name, data):

                    if table_name not in db.keys():
                        print(f'Таблиці з іменем {table_name} не існує.')
                        continue

                    if len(data) != len(db[table_name].columns):
                        print(f'Кількість аргументів ({len(data)}) не відповідає кількості стовпців таблиці ({len(db[table_name].columns)}).')
                        continue

                    db[table_name].insertInto(data)
                    print(f'1 рядок було додано в таблицю {table_name}')

            case select if select.lower().startswith('select from'):
                if command.count(' ') == 1:
                    print('Відсутні аргументи після SELECT FROM.')
                    continue

                command = re.sub('select from ', '', command, 1)
                condition = None
                
                try:
                    index = command.lower().index('where')
                    table_name = command[:index-1]
                    condition = command[index+6:]
                except ValueError:
                    table_name = command

                if cr.selectFrom(table_name, condition):
                    pass
                    
                print(table_name, condition)
            case _:
                print('Команди не існує.')
                continue



start_session()