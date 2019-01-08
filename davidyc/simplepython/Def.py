def sum(a, b):
    return a+b

sumnum = sum(3,4)
print("Sum = ", sumnum)

x = 50
def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

func(x)
print('x по прежнему', x)


x = 50
def func():
    global x
    print('x равно', x)
    x = 2
print('Заменяем глобальное значение x на', x)

func()
print('Значение x составляет', x)


def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)

def printMax(x, y):
    '''Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__)














