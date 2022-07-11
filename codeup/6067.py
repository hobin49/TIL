a = int(input())

if a % 2 == 0 and a < 0:
    print("A")
elif a % 2 == 1 and a < 0:
    print("B")
elif a % 2 == 0 and a > 0:
    print("C")
else:
    print("D")