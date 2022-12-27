"""
Написать функцию readlog, которая примет аргументом имя файла, прочитает его содержимое
если в содержимом есть хоть одна строка error - вернет False
если нету - True

"""
"""
class firstError(Exception):
    pass

def readlog(file):
    try:
        f = open(file, "r")
        lines = f.readlines() # записывается в список lines
        for i in range(len(lines)): # итерации по количеству строк
            for word in lines[i].split(): # итерации по каждой строке
                if word == "error":
                    f.close()
                    raise firstError
    except firstError as error:
        print("False")
    else:
        print("True")

readlog("myfile")

"""

def read_log(filename):
    try:
        f = open(filename, "r")
        lines = f.readlines()
    except FileNotFoundError:
        print("No such File")
        return False
    for line in lines:
        if 'error' in line:
            return False
    return True

print(read_log("myfile"))