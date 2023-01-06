class ToyClass:
    def instancemethod(self):
        return 'instance method alled', self

    @classmethod
    def classmethod(cls):
        return 'class metod called', cls

    @staticmethod
    def staticmethod():
        return 'staticmethod called'

t1 = ToyClass ()
print(t1.instancemethod())
print(t1.classmethod())
print(t1.staticmethod())
