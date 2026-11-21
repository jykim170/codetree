fa, fs = input().split()
sa, ss = input().split()

if int(fa) >= 19 and fs == 'M':
    print(1)
elif int(sa) >= 19 and ss == 'M':
    print(1)
else:
    print(0)