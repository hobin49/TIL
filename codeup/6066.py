a, b, c = map(int, input().split())

num = [a, b ,c]

for i in range(len(num)):
    if num[i] % 2 == 0:
        print("even")
    else:
        print("odd")