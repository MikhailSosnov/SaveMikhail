print('Калькулятор_У')

oper = ' '
while (oper != "+") and (oper != "-") and (oper != "*") and (oper != "/") and (oper != "**"):
    oper = input("Введите символ операции +,-,*,/,** ")
    print(oper)

x = y = 1.1

while 'true':
    try:
        x = float(input("Введите первое число: "))
        break
    except:
        print("Вы ввели не число, ")
        continue

while 'true':
    while 'true':
        try:
            y = float(input("Введите второе число: "))
            break
        except:
            print("Вы ввели не число, ")
            continue
    if (oper == "/") and (y == 0):
        print("На 0 делить нельзя, ")
        continue
    break

if (oper == "+"):
    z = x + y

if (oper == "-"):
    z = x - y

if (oper == "*"):
    z = x * y

if (oper == "/"):
    z = x / y

if (oper == "**"):
    z = x ** y

print("Результат :" + str(z))

