n = int(input())
s = 0
c = 0

while True:
    s += c
    c += 1
    if s >= n:
        break

print(s)