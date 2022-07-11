r, g, b = map(int, input().split())

raw = (r * g * b / 8 / 1024 / 1024)

print('%.2f'% raw, "MB")