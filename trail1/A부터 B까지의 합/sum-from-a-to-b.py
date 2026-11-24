w = 0

a, b = map(int, input().split())

for i in range(a, b+1):
    w += i
print(w)