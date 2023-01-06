try:
    text = input('Input somthing: ')
except EOFError:
    print('What for do EOF?')
except KeyboardInterrupt:
    print('You cancel operation.')
else:
    print ('You enter {0}'.format(text))
    u