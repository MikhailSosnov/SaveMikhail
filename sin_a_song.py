song_Afonas = '''Маленкий хрюкасий,
Котенок Афанасий.
Мявкает: Хрю, хрю...
На свинью, на большую свинью!'''

f = open ('song_Afonas.txt', 'w')
f.write(song_Afonas)
f.close()

f = open('song_Afonas.txt','r')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end = '')

f.close()



