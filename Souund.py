import functools

from functools import total_ordering

@total_ordering
class Real_string:
    def __init__(self, some_str):
        self.some_str = str(some_str)

    def __eq__(self, other):
        if not isinstance(other, Real_string):
            other = Real_string(other)
        return len (self.some_str) == len(other.some_str)

    def __lt__(self, other):
        if not isinstance(other, Real_string):
            other = Real_string(other)
        return len(self.some_str) < len(other.some_str)

    def __le_(self, other):
        return self == other or self < other


str1 = Real_string('Молоко')
str2 = Real_string('Абрикоосы растут')
str3 = 'Gold'
str4 = [1, 2, 3]

print(str1 < str4)
print(str1 >= str2)
print(str1 == str3)


s1 = Real_string('r Ect')

print(s1.some_str)


    # def name_age(self, age = 33):