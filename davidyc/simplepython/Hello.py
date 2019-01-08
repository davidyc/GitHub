print("hello")
# comment print("hello")
string = 'it is string'
print(string)
string2 = "hello world"
string3 = string +  string2
print(string3)
print("this is first string {0}".format(string))        
str = '''This is multi
string '''
print(str)
num = 3
num2 = 5
num3 = 45
numsum = 12 + num2
print(numsum)
print('num sum = ' , numsum + num3, " eeeee")

number = 23
guess = int(input('Введите целое число : '))
if guess == number:
    print('Поздравляю, вы угадали,') # Здесь начинается новый блок
    print('(хотя и не выиграли никакого приза!)') # Здесь заканчивается новый блок
elif guess < number:
    print('Нет, загаданное число немного больше этого.') # Ещё один блок
# Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
# чтобы попасть сюда, guess должно быть больше, чем number
    print('Завершено')
# Это последнее выражение выполняется всегда после выполнения оператора if

number = 23
running = True              
while running:
    guess = int(input('Введите целое число : '))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')    
# Здесь можете выполнить всё что вам ещё нужно
print('Завершение.')

for i in range(1,10):
    print("i = ", i)
else:
    print("Elvis left build")

while True:
    s = input('Введите что-нибудь : ')
    if s == 'out':
        break
    print('Длина строки: ', len(s))
print('Завершение')


