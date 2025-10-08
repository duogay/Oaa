import grammar as g

def createTable(table_name, args):

    if g.checkSpelling(table_name):
        return print(f'Неправильний синтаксис назви таблиці: {table_name}')
    
    if len(args) != len(set(args)):
        return print(f'Назви стовпчиків не можуть повторюватись.')

    for arg in args:
        if g.checkSpelling(arg):
            print(f'Неправильний синтаксис назви стовпчику: {arg}')
            return False
    return True
        
def insertInto(table_name, args):

    if g.checkSpelling(table_name):
        print(f'Неправильний синтаксис назви таблиці: {table_name}')
        return False
    
    for arg in args:
        if g.checkTableValues(arg):
            print(f'Неправильний синтаксис значення стовпчику: {arg}')
            return False
    return True

def selectFrom(table_name, condition):
    
    if g.checkSpelling(table_name):
        print(f'Неправильний синтаксис назви таблиці: {table_name}')
        return False
    
        