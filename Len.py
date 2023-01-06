class MyClass:
    def __init__(self, txt):
        self.name = txt

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __index__(self):
        p = self.name.count(' ') + 1
        return p

    def __round__(self):
        self.name = 'reset meaning'
        return self

txt = 'jne, two, three, four, five '
txt += '\ngo on rabbit to play'

obj = MyClass(txt)
print(obj)

print('Lettar ', len(obj))

print('Word', obj.__index__())

print('Bin ', bin(obj))

print('Eight ', oct(obj))


print(obj.__round__())
print(obj)