a, b = map(int, input().split())

w = 0

for i in range(min(a, b), max(a, b)+1):
    if i % 5 == 0:
        w += i

print(w)