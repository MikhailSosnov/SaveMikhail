class MutFunc:
    u = 4

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum_f(self):
        z = self.a + self.b
        print(z)
        self.z = z

    def multi_f(self):
        w = self.c * self.z
        self.w = w - MutFunc.u

    def pr_f(self):
        print(self.w)

class SubFunc(MutFunc):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def power(self):
        s = (m_f1.w) ** (self.x)
        print(s)
        s = s/self.y
        self.s = s
        print(self.s)
        print(__name__)
        # print(dir())



m_f1 = MutFunc(6, 3, 11)
s_f1 = SubFunc(2, 10)

m_f1.sum_f()
m_f1.multi_f()
m_f1.pr_f()

s_f1.power()

dir()
#
# print(- MutFunc.u)
#
# print(m_f1.w)







