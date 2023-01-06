def fib_fak():

    # Блок ввода даты

    while True:

        date_str = input("Введите натуральное число: ")

        try:
            date_int = int(date_str)
            if int(date_str) >= 1:
                 break
            else:
                print("Число введено не корректно")
                continue

        except:
            print("Число введено не корректно")
            continue

    print(date_int)

    sum = 1
    sum_next =1

    for i in range(0, date_int):
        sum_posr = sum_next
        sum_next = sum + sum_next
        sum = sum_posr
        print(i+1, ' итерация ', sum_next)

    print(' ')

    fak = 1
    fak_next = 1

    for i in range(0, date_int):
        fak_next = fak * (i+1)
        fak = fak_next
        # print(i + 1, ' итерация ', fak_next)

    print('Выполнено ', i+1, 'итераций', 'Факториал ', i+1,'! = ', fak_next)



while True:

    fib_fak()

    weit = input("For QUIT press Q / for continue press other key (end press Enter) ")
    print (" ")

    if (weit == "Q") or (weit == "q") or (weit == "Й") or (weit == "й"):
        break

print (" ")
print("Программа окончена")

