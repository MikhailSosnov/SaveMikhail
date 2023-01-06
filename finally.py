import time

try:
    f = open('song_Afonas.txt', 'r')
    while True:
        line = f.readline()
        if len(line) ==0:
            break
        print(line, end = '')
        time.sleep(3)
        time.sleep(3)
except KeyboardInterrupt:
    print ('You cancel read the file')
finally:
    f.close()
    print('\nClean and close the file')

