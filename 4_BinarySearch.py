def Bin_Sear():

    # .datetime()
    import datetime as DT

    date_now = DT.datetime.now()
    date_begin = DT.datetime.strftime(date_now, '%d.%m.%Y %H:%M:%S')

    print('Загадайте целое число от 1 до 100')

    wait = input('Когда загадали число нажмите Enter',)

    print('Время начала угадывания: ', date_begin)

    unknown = 50

    unknown_top = 100

    unknown_bottom = 0

    cycle=0

    while True:

        cycle +=1

        print ('Загаданное число равно', unknown)
        choice = input('Если "Да" нажмите - Y, если "Меньше" - L, если "Больше" - R')

        print('Ваш выбор ', choice)

        if (choice == "Y") or (choice == "y") or (choice == "Н") or (choice == "н"):

            date_now = DT.datetime.now()
            date_begin = DT.datetime.strftime(date_now, '%d.%m.%Y %H:%M:%S')
            print('Время окончания угадывания: ', date_begin)

            print ('Мы угадали с ', cycle, 'раза')
            break

        elif (choice == "L") or (choice == "l") or (choice == "Д") or (choice == "д"):
            unknown_top = unknown
            unknown = round((unknown + unknown_bottom)/2)
            continue

        elif (choice == "R") or (choice == "r") or (choice == "К") or (choice == "к"):
            unknown_bottom = unknown
            unknown = round((unknown_top + unknown)/2)
            continue

while True:

    Bin_Sear()

    wait = input("For QUIT press Q / for continue press other key (end press Enter) ")
    print (" ")

    if (wait == "Q") or (wait == "q") or (wait == "Й") or (wait == "й"):
        break

print (" ")
print("Программа окончена")

