a, b = map(int, input().split())

w = 0
p = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        w += i
        p += 1
    
print(w, f'{(w/p):.1f}')