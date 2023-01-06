class MyClass:
    def __init__(self, nums):
        self.nums = list()
        for n in nums:
            self.nums.append(n)

    def __str__(self):
        txt = 'Meaning fild-list -'
        for n in self.nums:
            txt +=str(n) + '1'
        return txt

    def __int__(self):
        return len(self.nums)

    def __float__(self):
        avr = sum(self.nums)/int(self)
        return avr

    def __bool__(self):
        if int(self)%2 == 0:
            return True
        else:
            return False
    def __complex__(self):
        mn = min(self.nums)
        mx = max(self.nums)
        z = complex(mx, mn)
        return z

obj1 = MyClass({2.8,4.1,7.5,2.5,9.3, 6.6})
print(obj1)
print('Elements in list -', int(obj1))
if obj1:
    print('четное кол эл')
else:
    print('не четное кол эл')
print('Averig', float(obj1))
print('min, max ', complex(obj1))

# print(MyClass(3))

