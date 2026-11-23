A, B = map(int, input().split())

integer = A // B
remainder = A % B

print(integer, end=".")

for i in range(20):
    remainder *= 10
    digit = remainder // B
    print(digit, end="")
    remainder %= B