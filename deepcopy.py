from copy import copy, deepcopy

class MyClass:
    def __init__(self, name, nums):
        self.name = name
        self.nums = nums

    def show(self):
        print('name - ', self.name)
        print('nums - ', self.nums)

m1 = MyClass('Python', [1, 2, 3])
m1.show()

y = copy(m1)
z = deepcopy(m1)

y.show()
z.show()


m1.name = 'Java'
m1.nums[0] = 8

# y = copy(m1)
# z = deepcopy(m1)

y.show()
z.show()



