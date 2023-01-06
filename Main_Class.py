class MainClass:
    main_text = 'Родительский текст'
    def __init__(self, sub_text = 'Другой текст'):
        self.sub_text = sub_text

    def chaing(self, chaing1 = 4):
        self.chaing1 = chaing1

class ChildrenClass(MainClass):
    def __init__(self, m_text = MainClass().main_text, s_text = MainClass().sub_text, number = 8):
        self.s_text = s_text
        self.m_text = m_text
        self.number = number

# M1 = MainClass()
# print(M1.main_text)
# print(M1.sub_text)bkj
# print(MainClass().sub_text)
# # .main_text = ' hhh'

MainClass.main_text = 'ttt'
print(MainClass().main_text)

MainClass().sub_text = ' uuu'
print(MainClass().sub_text)

MainClass.chaing1 = 88
print(MainClass().chaing1)


C1 = ChildrenClass('Смысл Вселенной', 'число:', 42)
print(C1.m_text)
print(C1.s_text)
print(C1.number)

# C2 = ChildrenClass()
# print(C2.main_text)
# print(C2.s_text)
# print(C2.number)

