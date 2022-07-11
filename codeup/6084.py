h, b, c, s = map(int, input().split())

raw = (h * b * c * s) /8/ 1024 / 1024

print(f'{raw:.1f} MB')
