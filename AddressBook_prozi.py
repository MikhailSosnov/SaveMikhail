import pickle
address_book = 'address_book.data'
dic_cards = {}

try:
    with open(address_book, 'rb') as f:
        stored_list = pickle.load(f)
        print(stored_list)
except EOFError:
    store_list = {}

name = input('ФИО: ')
address= input('Адресс: ')
dic_cards[name] = address

try:
    with open(address_book, 'rb') as f:
        stored_list = pickle.load(f)
except EOFError:
    stored_list = {}

with open(address_book, 'wb') as f:
    dic_sum = {**stored_list, **dic_cards}
    pickle.dump(dic_sum, f)
    print(dic_sum)
