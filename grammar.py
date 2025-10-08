import re

def checkSpelling(data):
    if len(data) == 1:
        if not data.isalpha():
            return True
        return False
    
    try:
        if not data[0].isalpha() or not bool(re.fullmatch(r'[a-zA-Z_0-9]+', data[1:])):
            return True
    except IndexError:
        return True
    
    return False

def checkTableValues(data):
    try:
        if not data[0] == data[-1] == '"':
            return True
    except IndexError:
        return True

    if len(data) == 3:
        if not data[1].isalpha():
            return True
        return False
    
    try:
        if not data[1].isalpha() or not bool(re.fullmatch(r'[a-zA-Z_0-9]+', data[2:-1])):
            return True
    except IndexError:
        return True
    return False

