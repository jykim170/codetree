n = int(input())

s = 0
t = 0
for _ in range(n):
    a = int(input())
    s += a
    t += 1

print(s, f'{(s/t):.1f}')