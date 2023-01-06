class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Input somthing: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('What for do EOF?')
except ShortInputException as ex:
    print('ShortInputException: Length string -- {0}; \
          wait min {1}'.format(ex.length, ex.atleast))
else:
    print ('Not Exception')
