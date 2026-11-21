n = int(input())

judge = 'false'
if n % 2 == 1 and n % 3 == 0 :
    judge = 'true'

if n % 2 == 0 and n % 5 == 0:
    judge = 'true'

print(judge)