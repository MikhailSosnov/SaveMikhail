# print('Индекс массы тела - ИМТ')

def IMT_old():

    while True:
        try:
            weight = float(input("Введите свой вес (кг): "))
            break
        except:
            print("Вы ввели не число, ")
            continue

    while True:
        while True:

            try:
                height = float(input("Введите свой рост (м): "))
                break
            except:
                print("Вы ввели не число, ")
                continue

        if height == 0:
            print("На 0 делить нельзя, ")
            continue

        if ((height > 2.72) and (height < 45)) or (height < 0.45) or (height > 272):
            print ("Это не человеческий рост, повторите ввод !")
            continue

        break

    if height > 2.72:
        height = height / 100
        print("Вероятно Вы ввели рост в сантиметрах, мы перевели в метры: ", height)

    while 'true':
        try:
            old = float(input("Введите свой возраст (лет)): "))
            break
        except:
            print("Вы ввели не число, ")
            continue

    print(' ')

    IMT = weight / (height ** 2)

    print("Индекс массы тела = ", IMT)

    if IMT <= 16:
        print("Выраженный дефицит массы тела")

    elif (IMT > 16) and (IMT <= 18.5):
        print("Недостаточная (дефицит) маса тела")

    elif (IMT > 18.5) and (IMT <= 25):
        print("Норма")

    elif (IMT > 25) and (IMT <= 30):
        print("Избыточная маса тела (предожирение)")

    elif (IMT > 30) and (IMT <= 35):
        print("Ожирение первой степени")

    elif (IMT > 35) and (IMT <= 40):
        print("Ожирение второй степени")

    elif IMT > 40:
        print("Ожирение третьей степени(морбидное)")

    print(' ')

    if old <= 1:
        age = "Младенец"

    elif (old > 1) and (old <= 10):
        age = "Ребенок"

    elif (old > 10) and (old <= 18):
        age = "Подросток"

    elif (old > 18) and (old <= 60):
        age = "Взрослый"

    elif old > 60:
        age = "Пожилой"

    print("Возрастная категория:", age)
    print (" ")

while True:
    IMT_old()
    weit = input("For QUIT press Q / for continue press other key (end press Enter) ")
    print (" ")

    if (weit == "Q") or (weit == "q") or (weit == "Й") or (weit == "й"):
        break

print (" ")
print("Программа окончена")
