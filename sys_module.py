import sys
print(dir(sys))

z = sys.path

print(sys.path)

print(len(sys.path))
for q in range(0,len(sys.path)):
    print(sys.path [q])

print("Аргументы командной строки:")

for i in sys.argv:
    print(i)

print(__name__)

dir(sys)