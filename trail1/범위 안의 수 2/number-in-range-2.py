w = 0
s = 0

for _ in range(10):
    a = int(input())
    if 0 <= a <= 200:
        w += a 
        s += 1

print(w, f'{(w/s):.1f}')