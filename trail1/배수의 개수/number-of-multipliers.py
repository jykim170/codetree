tcnt, fcnt = 0, 0
for i in range(10):
    a = int(input())
    if a % 3 == 0:
        tcnt += 1
    
    if a % 5 == 0:
        fcnt += 1
    
print(tcnt, fcnt)
