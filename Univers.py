class Univers:
    None
def answer():
    return 43

print(answer())

u = Univers()
u.answer = 21
print(u.answer)
answer.answer = 22
print(answer.answer)

print(u.answer + answer.answer == answer())