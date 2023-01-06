def date_conversion():
    import datetime as DT

    import re

    # Блок ввода даты

    while True:

        date_str = input("Введите дату в формате dd/mm/yyyy : ")

        try:
            date_date = DT.datetime.strptime(date_str, '%d/%m/%Y').date()
            date_full = DT.datetime.strftime(date_date, '%d/%m/%Y')
            break

        except:
            print("Дата введена не корректно")
            continue

    date_year = int(DT.datetime.strftime(date_date, '%Y'))

    if ((date_year % 4 == 0) and (date_year % 100 != 0)) or (date_year % 400 == 0):

        year_name = 'високосный'

    else:

        year_name = 'не високосный'


    print('Введенная дата - ', date_full, ' - год ', year_name)

    # Блок вывода года и его названия по востчному календарю

    gor = {
        0: 'Крысы',
        1: 'Быка',
        2: 'Тигра',
        3: 'Кролика',
        4: 'Дракона',
        5: 'Змеи',
        6: 'Лошади',
        7: 'Козы',
        8: 'Обезьяны',
        9: 'Петуха',
        10: 'Собаки',
        11: 'Свиньи'
    }

    date_year = DT.datetime.strftime(date_date, '%Y')

    # print(date_year, '- год:')

    if int(date_year) - 2008 >= 0:
        year_0_11 = (int(date_year) - 2008) % 12
        # print(year_0_11)
        print(date_year, '- год:', gor[year_0_11])
    elif int(date_year) - 2008 < 0:
        year_0_11 = 12 - abs((int(date_year) - 2008)) % 12
        # print(year_0_11)
        print(date_year, '- год:', gor[year_0_11])

    date_month = int(DT.datetime.strftime(date_date, '%m'))

    # Блок вывода номера квартала

    if date_month in [1, 2, 3]:
        print('1 квартал')
    elif date_month in [4, 5, 6]:
        print('2 квартал')
    elif date_month in [7, 8, 9]:
        print('3 квартал')
    elif date_month in [10, 11, 12]:
        print('4 квартал')

    # Блок преобразования номера месяца в его название

    month_dic = {
        0: 'Январь',
        1: 'Февраль',
        2: 'Март',
        3: 'Апрель',
        4: 'Май',
        5: 'Июнь',
        6: 'Июль',
        7: 'Август',
        8: 'Сентябрь',
        9: 'Октябрь',
        10: 'Ноябрь',
        11: 'Декабрь'
    }

    print('Месяц - ', month_dic[date_month - 1])

    # День

    date_day = int(DT.datetime.strftime(date_date, '%d'))

    print('День в месяце - ', date_day)

    # Дней с начала года

    date_begin_year_str = '01/01/' + str(DT.datetime.strftime(date_date, '%Y'))

    date_begin_year_date = DT.datetime.strptime(date_begin_year_str, '%d/%m/%Y').date()

    # print(date_date)
    # print(str(date_begin_year_date))

    day_delta = (date_date - date_begin_year_date).days

    print('Количество дней, прошедее с начала года - ', day_delta)

    # День недели

    day_week_number = DT.datetime.weekday(date_date)

    week_dic = {
        0: 'Понедельник',
        1: 'Вторник',
        2: 'Среда',
        3: 'Четверг',
        4: 'Пятница',
        5: 'Суббота',
        6: 'Воскресенье'
    }

    print('День недели - ', week_dic[day_week_number])



while True:

    date_conversion()

    weit = input("For QUIT press Q / for continue press other key (end press Enter) ")
    print (" ")

    if (weit == "Q") or (weit == "q") or (weit == "Й") or (weit == "й"):
        break

print (" ")
print("Программа окончена")
