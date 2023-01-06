class Myclass:
    def __setattr__(self, attr, val):
        print('Exequte metod _setattr__')
        txt = '*\tField - ' +str(attr)
        txt += ' assign value: ' +str(val)
        print(txt)
        self.__dict__[attr] = val
        print('Metod __setattr exequte')

    def __getattribute__(self, attr):
        print ('Exequte metod __get_attribute: ')
        txt = '*\tRead value field - ' + str(attr)
        print(txt)
        try:
            res = object.__getattribute__(self, attr)
        except AttributeError:
            res = 'At exampl field ' + str(attr) + ' not'
        print('Method __getattribute__ end work.')
        return res

    def __delattr__ (self, attr):
        print('Execute method __delattr__ : ')
        txt = '*\tErase field ' + str(attr)
        print(txt)
        try:
            del self.__dict__[attr]
        except KeyError:
            print('can not delete field ', str(attr))
        print('Method __delattr_ execut')


m1 = Myclass()
m1.name = 'Python'
print('meaning field: ', m1.name)
del m1.name
print(m1.name)
del m1.name

# print(m1.__getattribute__(10))
# print(m1.__setattr__(3, 7))