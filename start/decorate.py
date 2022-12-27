"""
Написать функцию, которая "обернет" слово, передаваемое в параметре в тэг <html>.
Пример:
myfunction("hello") -> "<html>hello<html>"

"""

def html_decorate(func):
    def wrapper_func(*args):
        print('<html>', *args, '<html>')
    return wrapper_func

@html_decorate
def myfunction(parameter):
    print(parameter)

myfunction('Hello')