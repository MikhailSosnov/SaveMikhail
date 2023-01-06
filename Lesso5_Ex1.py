class Myclass:
    Nmax = 6

    def __init__(self,nums):
        n = Myclass.Nmax
        self.nums = [0 for i in range(n)]
    def __str__(self):
        txt ='|'
        for s in self.nums:
            txt += ' ' + str(s) + '|'
        return txt

    def __setitem__(self, i, v):
        k = i % len(self.nums)
        self.nums[k] = v
        return self.nums[k]

    def __getitem__(self,i):
        k = i % len(self.nums)
        return self.nums[k]

    def __delitem__(self, i):
        k = i % len(self.nums)
        self.nums[k] = '*'


print(Myclass.Nmax)

m1 = Myclass(1)
print(m1.nums)
m1[0] = 100
m1[2] = -3
m1[24] = 123
print(m1)

print('index 4', m1[4])
print('index 0', m1[0])
print(m1)

del m1[0]
print(m1)

print(m1.__setitem__(1,3))

#
# print(m1.__str__())
# print(m1.__setitem__)
# print(m1.__getitem__(410001))





