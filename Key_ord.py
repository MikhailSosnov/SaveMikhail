# '''Програмки с возвратом названия/кода нажатой клавиши без дополнительного нажатия Enter
#    Верхняя работат везде. Закомментиованная работает из коммандной строки, в PyCharm не работает.''

import keyboard

print ('Print any Kay: ')

def print_pressed_keys(e):

    # print(e, e.event_type, e.name)
    # закомметирована более мощная (избыточно) комманда

    print(type(e.name))
    print(e.name)

    if e.name == 'y':
        print('iii')

keyboard.hook(print_pressed_keys)
keyboard.wait()

# import msvcrt

# while True:
    # kye_ord1 = ord(msvcrt.getch())
    # print('Код клавиши: ', key_ord1)
    #
    # if kye_ord1 == 27:
    #     break

    # wait = input("For QUIT press Q / for continue press other key (end press Enter) ")
    # print(" ")
    #
    # if (wait == "Q") or (wait == "q") or (wait == "Й") or (wait == "й"):
    #     break
    #
    # print('Код клавиши: ', ord(msvcrt.getch()))
