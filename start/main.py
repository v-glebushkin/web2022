"""
x=4
y=10

if x<5 and y>9:
    print ('x < 5') # 4 пробела табуляция, таб не желательно, он может быть разным в разных IDE
elif x >5:
    print('x > 5')
else:
    print ('x = 5')


a=[1,2,3,4,5]
for i in a:
    print(i**2)

"""

"""
a={1:'one', 5: 'five', 7: 'seven', 10: 'ten', 15: 'fifteen'} #словарь
for i in a.keys():
    if i > 5:
        break #выход из цикла
    if i == 10:
        continue #пропуск итерации, но программа возвращается к началу цикла
    print(i)

"""

"""
for i in range(10):
    print(i)

for i in [1,2,3]:
    print(i)

for i in range(10,20):
    print('range ' + str(i))


def funct(x, y=5, **kwargs): #kwargs отправляет все лишнее в словарь
    return str(x**2), y, kwargs
print(funct(3,9,n=10,w=12)) #надо обязательно именовать

"""



max_number = lambda a, b: a if a > b else b
print(max_number(3,5))


def four():
    x = 0
    while x < 4:
        print('in gen, x = ', x)
        yield x # хранит значение локальной переменной, пока цикл не выполнится
        x += 1

for i in four():
    print(i)


"""Декоратор (изменение функции, не трогая саму функцию)"""

def decorate(func):
    print('in decorate')
    def wrapper_func(*args): # *args обрабатывает все необработанные аргументы
        print('executing', func.__name__)
        return func(*args)
    return wrapper_func

@decorate #второй вариант, более удобо-читаемый
def myfunction(parameter):
    print(parameter)

def main(): # правило хорошего тона - брать основной код в функцию main
    #myfunction = decorate(myfunction) #первый вариант
    myfunction('Hello')

"""В Python есть специальный прием, который позволяет указать, что какой-то код не должен
выполняться при импорте: все строки, которые находятся в блоке if __name__ == '__main__'
не выполняются при импорте. Переменная __name__ - это специальная переменная, которая будет
равна "__main__", только если файл запускается как основная программа, и выставляется равной
имени модуля при импорте модуля."""

if __name__ == '__main__':
    main()